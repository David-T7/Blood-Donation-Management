# Generated by Django 4.0.3 on 2022-04-26 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAccount', '0002_alter_address_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='address',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
