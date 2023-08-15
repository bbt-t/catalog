from django.urls import path

from catalog.views import (
    HomePageListView,
    ContactsPageView,
    AboutProductPageDetailView,
    AddProductPageView,
    accept_add, BlogPageListView, BlogPostPageDetailView, BlogPostCreateView, BlogPostUpdateView, accept_delete,
    BlogPostPageDeleteView
)

urlpatterns = [
    path("", HomePageListView.as_view(), name="homepage"),
    path("product/<int:id>/", AboutProductPageDetailView.as_view(), name="product-detail"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("add/", AddProductPageView.as_view(), name="add_product"),

    path("ok", accept_add, name="ok"),
    path("deleted", accept_delete, name="success_deleted"),

    path("blog/", BlogPageListView.as_view(), name="blog_page"),
    path("blog/add/", BlogPostCreateView.as_view(), name="create_post"),
    path("blog/<int:id>/", BlogPostPageDetailView.as_view(), name="post"),
    path("blog/edit/<int:id>/", BlogPostUpdateView.as_view(), name="edit_post"),
    path("blog/del/<int:id>/", BlogPostPageDeleteView.as_view(), name="del_post"),
]
