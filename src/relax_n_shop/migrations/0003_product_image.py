# Generated by Django 3.0.8 on 2020-08-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relax_n_shop', '0002_remove_product_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='allproducts/'),
        ),
    ]