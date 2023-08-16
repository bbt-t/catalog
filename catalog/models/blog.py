from django.db import models


class BlogArticle(models.Model):
    title = models.CharField(max_length=64, verbose_name="Заголовок")
    slug = models.SlugField(max_length=128, null=True, blank=True)
    content = models.CharField(max_length=1024, verbose_name="Контент")
    image_preview = models.ImageField(
        upload_to="images/",
        help_text="Images are here -> images/",
        null=True,
        blank=True,
        verbose_name="Изображение",
    )
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано?")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")
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
