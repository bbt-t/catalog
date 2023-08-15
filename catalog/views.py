from logging import warning as log

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.models import Product, BlogArticle
from catalog.services.crud import (
    save_feedback, get_contact_details, get_category_by_param, save_product, get_all_categories
)


def accept_add_product(request):
    """
    If the prod addition was successful.
    """
    return render(request, "../templates/catalog/accept_add.html")


class BlogPostCreate(CreateView):
    model = BlogArticle
    fields = "title", "content", "image_preview", "is_published"
    success_url = reverse_lazy("ok")

    def form_valid(self, form):
        if form.is_valid():
            new_entry = form.save()
            new_entry.slug = slugify(new_entry.title)
            new_entry.save()
        return super().form_valid(form)


class BlogPostUpdate(UpdateView):
    model = BlogArticle
    fields = "title", "content", "image_preview", "is_published"
    pk_url_kwarg = "id"

    def form_valid(self, form):
        if form.is_valid():
            new_entry = form.save()
            new_entry.slug = slugify(new_entry.title)
            new_entry.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post", args=(self.kwargs.get("id"),))


class HomePageListView(ListView):
    """
    Homepage render.
    """
    model = Product
    context_object_name = "product_items"


class BlogPageListView(ListView):
    model = BlogArticle
    context_object_name = "blog_posts"

    def get_queryset(self):
        """
        Return only is_published = True
        """
        q = super().get_queryset()
        return q.filter(is_published=True)


class BlogPostPageDetailView(DetailView):
    model = BlogArticle
    context_object_name = "blog_post"
    pk_url_kwarg = "id"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        obj.views_count += 1
        obj.save()
        if obj.views_count == 100:
            send_mail(
                'Поздравление',
                'УРА! УРА! у вас более 100 просмотров!',
                'wrusacc@yandex.ru',
                ['zlukcss@gmail.com'],
                fail_silently=False,
            )
        return obj


class AboutProductPageDetailView(DetailView):
    model = Product
    context_object_name = "product_detail"
    pk_url_kwarg = "id"


class ContactsPageView(View):
    """
    contacts route render and add info to DB.
    """

    template_name = "../templates/catalog/contact.html"

    def post(self, request, *args, **kwargs):
        """
        POST request.
        """
        _, username, phone, message = request.POST.values()
        log("Cообщение от {}, номер телефона: {} - {}".format(username, phone, message))

        param = {
            "username": username,
            "phone": phone,
            "message": message,
        }
        save_feedback(param)

        return render(request, self.template_name)

    def get(self, request, *args, **kwargs):
        """
        GET request.
        """
        context = {
            "contacts": get_contact_details(),
        }
        return render(request, self.template_name, context)


class AddProductPageView(View):
    template_name = "../templates/catalog/add_product.html"

    def post(self, request, *args, **kwargs):
        """
        Get info for save a new Product.
        """
        _, name, category_id, price, description = request.POST.values()
        param = {
            "pk": category_id,
        }
        selected_category = get_category_by_param(param)
        try:
            param_save = {
                "category": selected_category,
                "name": name,
                "description": description,
                "price": price,
                "image_preview": request.FILES.getlist("product_image")[0],
            }
            save_product(param_save)
        except Exception as e:
            print(e)
        else:
            return HttpResponseRedirect(reverse_lazy("ok"))

        return render(request, self.template_name)

    def get(self, request, *args, **kwargs):
        """
        GET request.
        """
        context = {
            "categories": get_all_categories(),
        }
        return render(request, self.template_name, context)
