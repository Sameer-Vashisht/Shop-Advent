# Generated by Django 4.2.3 on 2023-07-29 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_customer_alter_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='passwordl',
            new_name='password',
        ),
    ]
