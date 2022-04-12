# Generated by Django 4.0.3 on 2022-04-11 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blood', '0004_alter_blood_donor_id'),
        ('Hospital', '0007_alter_bloodrequest_request_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodrequest',
            name='Blood_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Blood.blood'),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='Hospital_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hospital.hospital'),
        ),
    ]