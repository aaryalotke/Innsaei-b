# Generated by Django 4.0 on 2023-01-12 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('backend', '0015_alter_appuser_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUserNONMEMBER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=100)),
                ('otp', models.IntegerField(blank=True, null=True)),
                ('role', models.CharField(default='Student', max_length=100)),
                ('description', models.CharField(default='', max_length=256)),
                ('achievements', models.CharField(default='', max_length=256)),
                ('github', models.CharField(default='', max_length=100)),
                ('linkedin', models.CharField(default='', max_length=100)),
                ('isverified', models.BooleanField(default=False)),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True, unique=True)),
                ('isMember', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]