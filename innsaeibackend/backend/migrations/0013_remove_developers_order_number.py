# Generated by Django 4.0.6 on 2022-12-27 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_alter_councilmembers_email_alter_developers_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developers',
            name='order_number',
        ),
    ]
