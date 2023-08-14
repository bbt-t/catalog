from django.contrib import admin

from catalog.models import Category, Product, ContactDetails, BlogArticle


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "pk", "name"


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "price", "category"
    list_filter = ("category",)
    search_fields = "name", "description"


@admin.register(ContactDetails)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "country", "inn", "address"


@admin.register(BlogArticle)
class BlogArticleAdmin(admin.ModelAdmin):
    list_display = "pk", "title", "slug", "content", "is_published"
    search_fields = "created_at", "is_published"
