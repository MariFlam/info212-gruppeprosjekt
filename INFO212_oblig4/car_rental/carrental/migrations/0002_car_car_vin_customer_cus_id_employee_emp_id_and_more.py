# Generated by Django 4.1.2 on 2022-10-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_vin',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='cus_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_location',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_make',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_model',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_rented',
            field=models.CharField(default='available', max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_year',
            field=models.CharField(default=None, max_length=50),
        ),
    ]