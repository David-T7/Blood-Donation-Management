# Generated by Django 4.0.3 on 2022-04-26 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='ProfilePic',
            field=models.FileField(blank=True, default='profilepic/defaultprofile.jpeg', null=True, upload_to='profilepic/'),
        ),
    ]
