# Generated by Django 3.1.7 on 2023-04-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0024_auto_20230401_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='councilurl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='council')),
                ('council', models.CharField(choices=[('SE', 'SE'), ('TE', 'TE'), ('BE', 'BE'), ('FACULTY ADVISORS ', 'FACULTY ADVISORS')], max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('order_number', models.IntegerField(blank=True, default=0)),
                ('insta_id', models.URLField(blank=True)),
                ('linked_in', models.URLField(blank=True)),
                ('email', models.URLField(blank=True)),
            ],
        ),
    ]
