# Generated by Django 2.2.3 on 2019-07-06 07:04

import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 6, 7, 4, 31, 380970)),
        ),
        migrations.AlterField(
            model_name='user',
            name='interests',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Adventure'), ('2', 'Food'), ('3', 'Tech'), ('4', 'Family'), ('5', 'Health'), ('6', 'Sports'), ('7', 'Film'), ('8', 'Books'), ('9', 'Dance'), ('10', 'Arts')], max_length=20),
        ),
    ]
