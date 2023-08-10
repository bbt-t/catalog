from logging import warning as log

from django.shortcuts import render
from django.views import View

from catalog.models import Feedback


class HomePageView(View):
    """
    index render.
    """

    template_name = "../templates/catalog/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ContactsView(View):
    """
    contacts route render and add info to DB.
    """

    template_name = "../templates/catalog/contacts.html"

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
