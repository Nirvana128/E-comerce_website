# Generated by Django 5.1.4 on 2024-12-24 13:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_rename_razorpay_order_id_payment_paypal_payment_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('paypal', 'PayPal'), ('cash', 'Cash')], default='paypal', max_length=10),
        ),
    ]