# Generated by Django 3.1.7 on 2021-05-02 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artmgmt', '0002_auto_20210502_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='sdate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
