# Generated by Django 4.1.5 on 2023-02-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCT', '0002_alter_p_details_p_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_details',
            name='p_label',
            field=models.CharField(default='NEW', max_length=20),
        ),
    ]
