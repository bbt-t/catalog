from logging import warning as log

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView

from catalog.models import Product, BlogArticle
from catalog.services.crud import save_feedback, get_contact_details, \
    get_category_by_param, save_product, get_all_categories


class HomePageListView(ListView):
    """
    Homepage render.
    """
    model = Product
    context_object_name = "product_items"


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


class BlogPageListView(ListView):
    model = BlogArticle
    context_object_name = "blog_posts"


def accept_add_product(request):
    """
    If the prod addition was successful.
    """
    return render(request, "../templates/catalog/accept_add.html")
