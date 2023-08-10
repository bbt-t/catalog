from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Feedback(models.Model):
    """
    Model for saving messages from users to DB.
    """

    username = models.CharField(
        max_length=64,
        help_text="The name entered by the user when sending the msg.",
    )
    phone = PhoneNumberField(
        db_index=True,
        help_text="The phone number entered by the user when sending the msg.",
    )
    message = models.TextField(
        max_length=512,
        help_text="The text entered by the user when sending the msg.",
    )
    create_at = models.DateTimeField(
        editable=False,
        auto_now_add=True,
        db_comment="Date and time when the question was created",
    )

    class Meta:
        db_table_comment = "Users feedback"


class Category(models.Model):
    name = models.CharField(max_length=128, help_text="Category name")
    description = models.CharField(max_length=512, help_text="Category description")

    def __str__(self):
        return self.name

    class Meta:
        db_table_comment = "Product categories"


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    price = models.PositiveBigIntegerField(blank=True, null=True)
    image_preview = models.ImageField(
        upload_to="images/",
        help_text="Images are here -> images/",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        help_text="This is a foreign key of the category",
    )
    create_at = models.DateTimeField(
        editable=False,
        auto_now_add=True,
        db_comment="Date and time when the product was created",
    )
    update_at = models.DateTimeField(
        auto_now=True,
        db_comment="Date and time when the product was updated",
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table_comment = "Goods"


class ContactDetails(models.Model):
    country = models.CharField(max_length=64)
    inn = models.SlugField(max_length=64)
    address = models.CharField(max_length=256)

    def __str__(self):
        return self.address

    class Meta:
        db_table_comment = "Contact details"
