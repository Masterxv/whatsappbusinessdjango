# Generated by Django 2.2.6 on 2019-11-27 18:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('messageprocess', '0024_auto_20191127_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageprocessmodel',
            name='message_uuid',
            field=models.TextField(default=uuid.UUID('2341e8f0-1144-11ea-9cc9-645a049d591d')),
        ),
    ]
