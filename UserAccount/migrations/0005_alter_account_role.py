# Generated by Django 4.0.3 on 2022-04-27 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAccount', '0004_alter_address_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='Role',
            field=models.CharField(blank=True, choices=[(None, 'SelectRole'), ('BBManager', 'BBManager'), ('Nurse', 'Nurse'), ('LabTechnician', 'LabTechnician'), ('HospitalRepresentative', 'HospitalRepresentative')], max_length=25, null=True),
        ),
    ]
