# Generated by Django 5.2.2 on 2025-06-19 12:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop2', '0005_alter_order_status_alter_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='shop2.orderstatus', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Общая сумма'),
        ),
    ]
