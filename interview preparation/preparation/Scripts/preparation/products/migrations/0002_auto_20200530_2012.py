# Generated by Django 3.0.6 on 2020-05-30 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='products',
            new_name='product',
        ),
    ]
