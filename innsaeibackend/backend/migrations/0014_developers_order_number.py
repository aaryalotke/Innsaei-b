# Generated by Django 4.0.6 on 2022-12-27 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_remove_developers_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='developers',
            name='order_number',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
