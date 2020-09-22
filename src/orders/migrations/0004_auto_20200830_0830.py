# Generated by Django 3.0.8 on 2020-08-30 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200830_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_total',
            field=models.DecimalField(decimal_places=2, default=45.0, max_digits=100),
        ),
    ]
