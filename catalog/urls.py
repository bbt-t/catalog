from django.urls import path

from catalog.views import HomePageView, ContactsView

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
]
