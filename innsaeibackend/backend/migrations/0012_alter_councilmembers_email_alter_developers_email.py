# Generated by Django 4.0.6 on 2022-12-27 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_rename_first_name_councilmembers_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='councilmembers',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='developers',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
