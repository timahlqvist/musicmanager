# Generated by Django 2.2.1 on 2019-06-11 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listrecords', '0002_auto_20190611_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='record_number',
            field=models.CharField(max_length=400),
        ),
    ]