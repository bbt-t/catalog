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
        verbose_name="Дата создания",
    )

    class Meta:
        db_table_comment = "Users feedback"
        ordering = ("create_at",)


class Category(models.Model):
    name = models.CharField(
        max_length=128,
        help_text="Category name",
    )
    description = models.CharField(
        max_length=512,
        help_text="Category description",
        verbose_name="Описание",
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table_comment = "Product categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(
        max_length=512,
        verbose_name="Описание",
    )
    price = models.PositiveBigIntegerField(
        blank=True,
        null=True,
        verbose_name="Цена",
    )
    image_preview = models.ImageField(
        upload_to="images/",
        help_text="Images are here -> images/",
        null=True,
        blank=True,
        verbose_name="Фото товара",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        help_text="This is a foreign key of the category",
        verbose_name="Категория товара",
    )
    create_at = models.DateTimeField(
        editable=False,
        auto_now_add=True,
        db_comment="Date and time when the product was created",
        verbose_name="Дата создания",
    )
    update_at = models.DateTimeField(
        auto_now=True,
        db_comment="Date and time when the product was updated",
        verbose_name="Обновлено",
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table_comment = "Goods"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("price",)


class ContactDetails(models.Model):
    country = models.CharField(max_length=64, verbose_name="Страна")
    inn = models.CharField(max_length=64, verbose_name="ИНН")
    address = models.CharField(max_length=256, verbose_name="Адрес")

    def __str__(self):
        return self.address

    class Meta:
        db_table_comment = "Contact details"
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"


class BlogArticle(models.Model):
    title = models.CharField(max_length=64, verbose_name="Заголовок")
    slug = models.SlugField()
    content = models.CharField(max_length=1024, verbose_name="Контент")
    image_preview = models.ImageField(
        upload_to="images/",
        help_text="Images are here -> images/",
        null=True,
        blank=True,
        verbose_name="Изображение",
    )
    is_published = models.BooleanField(verbose_name="Опубликовано?")
    views_count = models.PositiveIntegerField(verbose_name="Количество просмотров", default=0)
    create_at = models.DateTimeField(
        editable=False,
        auto_now_add=True,
        db_comment="Date and time when the post was created",
        verbose_name="Дата создания",
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table_comment = "Blog content"
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
