from django.urls import path

from catalog.views import (
    HomePageListView,
    ContactsPageView,
    AboutProductPageTemplateView,
    AddProductPageView,
    accept_add_product, BlogPage,
)

urlpatterns = [
    path("", HomePageListView.as_view(), name="homepage"),
    path("product/<int:id>/", AboutProductPageTemplateView.as_view(), name="product-detail"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("add/", AddProductPageView.as_view(), name="add_product"),

    path("ok", accept_add_product, name="ok"),

    path("blog/", BlogPage.as_view(), name="blog_page"),
]
