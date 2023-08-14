from logging import warning as log

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from catalog.models import Feedback, Product, ContactDetails, Category


class HomePageView(TemplateView):
    """
    Homepage render.
    """

    template_name = "../templates/catalog/home_base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = Product.objects.all()
        return context


class AboutProduct(TemplateView):
    template_name = "../templates/catalog/show_product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["product_detail"] = Product.objects.get(pk=self.kwargs["id"])
        return context


class ContactsView(View):
    """
    contacts route render and add info to DB.
    """

    template_name = "../templates/catalog/contact_base.html"

    def post(self, request, *args, **kwargs):
        """
        POST request.
        """
        _, username, phone, message = request.POST.values()
        log("Cообщение от {}, номер телефона: {} - {}".format(username, phone, message))

        new_entry = Feedback(username=username, phone=phone, message=message)
        new_entry.save()

        return render(request, self.template_name)

    def get(self, request, *args, **kwargs):
        """
        GET request.
        """
        context = {
            "contacts": ContactDetails.objects.get(),
        }
        return render(request, self.template_name, context)


class AddProduct(View):
    template_name = "../templates/catalog/add_product.html"

    def post(self, request, *args, **kwargs):
        """
        Get info for save a new Product.
        """
        _, name, category_id, price, description = request.POST.values()
        selected_category = Category.objects.get(pk=category_id)
        try:
            new_entry = Product(
                category=selected_category,
                name=name,
                description=description,
                price=price,
                image_preview=request.FILES.getlist("product_image")[0],
            )
        except Exception as e:
            print(e)
        else:
            new_entry.save()
            return HttpResponseRedirect(reverse("ok"))

        return render(request, self.template_name)

    def get(self, request, *args, **kwargs):
        """
        GET request.
        """
        context = {
            "categories": Category.objects.all(),
        }
        return render(request, self.template_name, context)


def accept_add_product(request):
    """
    If the prod addition was successful.
    """
    return render(request, "../templates/catalog/accept_add.html")
