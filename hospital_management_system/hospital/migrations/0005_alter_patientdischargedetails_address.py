# Generated by Django 4.1.3 on 2023-01-07 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "hospital",
            "0004_rename_doctorname_patientdischargedetails_doctorname_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="patientdischargedetails",
            name="address",
            field=models.CharField(max_length=255),
        ),
    ]