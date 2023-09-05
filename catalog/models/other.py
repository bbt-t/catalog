from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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


class Version(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар')
    number = models.PositiveSmallIntegerField(verbose_name='Номер версии')
    name = models.CharField(max_length=100, verbose_name='Название версии')
    status = models.BooleanField(default=True, verbose_name='Активная версия')

    def __str__(self):
        return f"{self.name}: {self.number}, {self.status}"

    def save(self, *args, **kwargs):
        if self.status:
            Version.objects.filter(product=self.product, status=True).update(status=False)
        super(Version, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
