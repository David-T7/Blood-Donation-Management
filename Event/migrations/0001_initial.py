# Generated by Django 4.0.3 on 2022-04-26 12:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('Camps_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('CampsName', models.CharField(max_length=10)),
                ('CampsWoreda', models.CharField(max_length=50)),
                ('CampsKebele', models.IntegerField()),
                ('city', models.CharField(max_length=255, null=True)),
                ('Location', models.CharField(max_length=1000, null=True)),
            ],
            options={
                'db_table': 'Camp',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('Event_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('EventName', models.CharField(max_length=10)),
                ('EventPlace', models.CharField(max_length=50)),
                ('EventTime', models.TimeField()),
                ('EventDate', models.DateField()),
                ('EventType', models.CharField(max_length=10)),
                ('EventPic', models.FileField(blank=True, default='events/defaultevent.png', null=True, upload_to='events/')),
            ],
            options={
                'db_table': 'Event',
            },
        ),
    ]
