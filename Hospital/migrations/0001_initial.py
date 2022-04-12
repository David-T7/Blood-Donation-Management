# Generated by Django 2.2.7 on 2022-03-26 10:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Blood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('Hospital_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('HospitalName', models.CharField(blank=True, max_length=20, null=True)),
                ('Woreda', models.IntegerField(blank=True, null=True)),
                ('Kebele', models.IntegerField(blank=True, null=True)),
                ('HospitalRepresentative', models.CharField(max_length=10)),
                ('PhoneNo', models.IntegerField(blank=True, null=True)),
                ('BranchNo', models.CharField(max_length=10)),
                ('City', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('Blood_Req_Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Conatact_NO', models.IntegerField(blank=True, null=True)),
                ('Blood_Group', models.CharField(blank=True, max_length=10, null=True)),
                ('Quantity', models.CharField(blank=True, max_length=10, null=True)),
                ('Request_Date', models.DateField()),
                ('Blood_id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='Blood.Blood')),
                ('Hospital_id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='Hospital.Hospital')),
            ],
        ),
    ]