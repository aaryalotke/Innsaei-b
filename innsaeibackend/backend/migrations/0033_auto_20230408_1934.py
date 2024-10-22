# Generated by Django 3.1.7 on 2023-04-08 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0032_auto_20230408_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='councilmembers',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='developers'),
        ),
        migrations.AddField(
            model_name='developers',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='developers'),
        ),
        migrations.AddField(
            model_name='events2',
            name='gallary_pic1_link',
            field=models.ImageField(blank=True, null=True, upload_to='developers'),
        ),
        migrations.AddField(
            model_name='events2',
            name='gallary_pic2_link',
            field=models.ImageField(blank=True, null=True, upload_to='developers'),
        ),
        migrations.AddField(
            model_name='events2',
            name='gallary_pic3_link',
            field=models.ImageField(blank=True, null=True, upload_to='developers'),
        ),
        migrations.AddField(
            model_name='events2',
            name='gallary_pic4_link',
            field=models.ImageField(blank=True, null=True, upload_to='developers'),
        ),
        migrations.AddField(
            model_name='events2',
            name='poster1',
            field=models.ImageField(blank=True, null=True, upload_to='developers'),
        ),
        migrations.AddField(
            model_name='events2',
            name='poster2',
            field=models.ImageField(blank=True, null=True, upload_to='developers'),
        ),
        migrations.AddField(
            model_name='events2',
            name='poster3',
            field=models.ImageField(blank=True, null=True, upload_to='developers'),
        ),
        migrations.AddField(
            model_name='upcomingworkshopmodels',
            name='PosterImage',
            field=models.ImageField(blank=True, null=True, upload_to='developers'),
        ),
    ]
