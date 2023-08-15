# Generated by Django 4.2.4 on 2023-08-15 17:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]