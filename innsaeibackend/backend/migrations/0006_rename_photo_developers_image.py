# Generated by Django 4.0.6 on 2022-10-23 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_developers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='developers',
            old_name='photo',
            new_name='image',
        ),
    ]