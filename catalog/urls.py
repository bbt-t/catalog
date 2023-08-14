from django.urls import path

from catalog.views import (
    HomePageView,
    ContactsView,
    AboutProduct,
    AddProduct,
    accept_add_product,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("product/<int:id>/", AboutProduct.as_view(), name="product-detail"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("add/", AddProduct.as_view(), name="add_product"),
    path("ok", accept_add_product, name="ok"),
]
