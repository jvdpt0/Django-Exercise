# Generated by Django 4.2 on 2023-07-21 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_address_author_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
    ]
