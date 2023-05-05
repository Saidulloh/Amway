# Generated by Django 4.2.1 on 2023-05-04 16:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('price', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='price')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
