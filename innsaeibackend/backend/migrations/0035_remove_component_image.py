# Generated by Django 3.1.7 on 2023-04-08 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0034_auto_20230408_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='image',
        ),
    ]