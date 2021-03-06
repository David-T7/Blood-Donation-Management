# Generated by Django 4.0.3 on 2022-04-26 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Donor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FininshedAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Appointment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Donor.appointment')),
            ],
            options={
                'db_table': 'FininshedAppointment',
            },
        ),
        migrations.CreateModel(
            name='DeferringList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Donor_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Donor.donor')),
            ],
            options={
                'db_table': 'DeferringList',
            },
        ),
    ]
