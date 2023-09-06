from django.db import models


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


class Version(models.Model):
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, verbose_name="Товар"
    )
    number = models.PositiveSmallIntegerField(verbose_name="Номер версии")
    name = models.CharField(max_length=100, verbose_name="Название версии")
    status = models.BooleanField(default=True, verbose_name="Активная версия")

    def __str__(self):
        return f"{self.name}: {self.number}, {self.status}"

    def save(self, *args, **kwargs):
        if self.status:
            Version.objects.filter(product=self.product, status=True).update(
                status=False
            )
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
