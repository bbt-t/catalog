# Generated by Django 4.2.4 on 2023-08-10 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=64)),
                ('inn', models.SlugField(max_length=64)),
                ('address', models.CharField(max_length=256)),
            ],
            options={
                'db_table_comment': 'Contact details',
            },
        ),
    ]
