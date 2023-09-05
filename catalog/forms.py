from django import forms
from django.core.exceptions import ValidationError

from catalog.models import BlogArticle, Version


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogArticle
        # только одно из fields, exclude
        # fields = "__all__" #  всё
        # fields = "title", "content", "image_preview", "is_published"
        exclude = "create_at", "views_count"


class ProductForm(forms.ModelForm):
    """
    Форма для модели Product
    Проверяет поля name и description на присутствие запрещенных слов
    """

    forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')

    class Meta:
        model = Product
        exclude = ('creation_date', 'change_date')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name').lower()
        for word in self.forbidden_words:
            if word in cleaned_data:
                raise ValidationError('Название содержит запрещенные слова!')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description').lower()
        for word in self.forbidden_words:
            if word in cleaned_data:
                raise ValidationError('Описание содержит запрещенные слова!')
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class VersionForm(forms.ModelForm):
    """
    Форма для модели Version
    """

    class Meta:
        model = Version
        fields = 'number', 'name', 'status'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'checkbox-left'
