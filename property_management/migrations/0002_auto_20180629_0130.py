# Generated by Django 2.0.6 on 2018-06-29 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userAuthentication', '0004_auto_20180629_0130'),
        ('property_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertydetail',
            name='Administrator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userAuthentication.Administrator'),
        ),
        migrations.AddField(
            model_name='propertydetail',
            name='Agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userAuthentication.RealEstateManagementAgency'),
        ),
        migrations.AddField(
            model_name='propertydetail',
            name='Availlable_units',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='propertydetail',
            name='Location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userAuthentication.Location'),
        ),
        migrations.AddField(
            model_name='propertydetail',
            name='Number_of_units',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='propertydetail',
            name='Occupied_units',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='propertydetail',
            name='Property_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='propertydetail',
            name='Property_overview_photo',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='propertydetail',
            name='Property_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='unitdetail',
            name='Is_occupied',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='unitdetail',
            name='Number_of_rooms',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='unitdetail',
            name='Property_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='property_management.PropertyDetail'),
        ),
        migrations.AddField(
            model_name='unitdetail',
            name='Unit_ID',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='unitdetail',
            name='Unit_size',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
