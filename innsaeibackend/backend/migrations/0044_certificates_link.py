# Generated by Django 3.1.7 on 2023-04-10 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0043_certificates_certificates'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificates',
            name='link',
            field=models.ImageField(blank=True, default='https://drive.google.com/uc?export=download&id=16L8AkuCuh5jTrLvZsIFscvGls8Yo_VEr', null=True, upload_to=''),
        ),
    ]