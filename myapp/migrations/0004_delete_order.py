# Generated by Django 4.2.4 on 2023-09-17 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_product_category_delete_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]