# Generated by Django 4.1.5 on 2023-02-06 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PRODUCT', '0001_initial'),
        ('DASHBOARD', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_to_cart',
            fields=[
                ('cart_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cust_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='DASHBOARD.customer_details')),
                ('p_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='PRODUCT.p_details')),
            ],
        ),
    ]
