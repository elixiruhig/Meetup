# Generated by Django 2.2.3 on 2019-07-10 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0016_auto_20190710_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='photo',
            field=models.ImageField(default='group_photos/film.jpg', upload_to='group_photos'),
        ),
        migrations.AlterField(
            model_name='meetup',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 10, 33, 3, 788616)),
        ),
    ]
