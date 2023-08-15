from django.urls import path

from catalog.views import (
    HomePageListView,
    ContactsPageView,
    AboutProductPageDetailView,
    AddProductPageView,
    accept_add_product, BlogPageListView, BlogPostPageDetailView
)

urlpatterns = [
    path("", HomePageListView.as_view(), name="homepage"),
    path("product/<int:id>/", AboutProductPageDetailView.as_view(), name="product-detail"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("add/", AddProductPageView.as_view(), name="add_product"),

    path("ok", accept_add_product, name="ok"),

    path("blog/", BlogPageListView.as_view(), name="blog_page"),
    path("blog/<int:id>/", BlogPostPageDetailView.as_view(), name="post"),

]
