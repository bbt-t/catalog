from catalog.models import Product, Category, ContactDetails, Feedback


def get_product_by_param(param: dict):
    return Product.objects.get(**param)


def get_all_products():
    return Product.objects.all()


def get_category_by_param(param: dict):
    return Category.objects.get(**param)


def get_all_categories():
    return Category.objects.all()


def get_contact_details():
    return ContactDetails.objects.get()


def save_feedback(params: dict):
    new_entry = Feedback(**params)
    new_entry.save()


def save_product(params: dict):
    new_entry = Product(**params)
    new_entry.save()
