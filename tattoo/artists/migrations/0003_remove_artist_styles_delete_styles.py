# Generated by Django 4.2 on 2023-06-07 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_alter_artist_styles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='styles',
        ),
        migrations.DeleteModel(
            name='Styles',
        ),
    ]