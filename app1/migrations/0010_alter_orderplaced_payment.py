# Generated by Django 5.1.4 on 2024-12-24 13:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_payment_created_at_payment_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.payment'),
        ),
    ]