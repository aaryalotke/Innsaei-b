# Generated by Django 3.1.7 on 2023-04-01 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0023_initiatives'),
    ]

    operations = [
        migrations.RenameField(
            model_name='initiatives',
            old_name='PosterImage',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='initiatives',
            old_name='EventName',
            new_name='Name',
        ),
    ]
