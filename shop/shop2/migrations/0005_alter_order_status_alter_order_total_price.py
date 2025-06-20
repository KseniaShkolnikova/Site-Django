# Generated by Django 5.2.2 on 2025-06-19 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop2', '0004_remove_cartitem_cart_remove_cartitem_menu_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shop2.orderstatus', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Общая сумма'),
        ),
    ]
