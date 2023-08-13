from django.urls import path

from catalog.views import HomePageView, ContactsView, AboutProduct

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("product/<int:id>/", AboutProduct.as_view(), name="product-detail"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
]
