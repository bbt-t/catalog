from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    """
    Delete all data in DB.
    """

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
