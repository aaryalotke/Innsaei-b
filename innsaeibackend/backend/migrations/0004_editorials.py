# Generated by Django 4.0.6 on 2022-10-20 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='editorials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editorial_name', models.CharField(max_length=100)),
                ('editorial_link', models.URLField()),
            ],
        ),
    ]