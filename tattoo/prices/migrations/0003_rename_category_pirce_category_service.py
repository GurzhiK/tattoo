# Generated by Django 4.2 on 2023-06-07 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0002_category_pirce_service_price_delete_price_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category_pirce',
            new_name='Category_service',
        ),
    ]