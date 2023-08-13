from logging import warning as log

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from catalog.models import Feedback, Product


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
        return render(request, self.template_name)
