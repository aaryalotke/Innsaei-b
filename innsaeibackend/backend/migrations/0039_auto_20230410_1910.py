# Generated by Django 3.1.7 on 2023-04-10 13:40

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0038_auto_20230410_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appusernonmember',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='9999999990', max_length=128, null=True, region=None),
        ),
    ]