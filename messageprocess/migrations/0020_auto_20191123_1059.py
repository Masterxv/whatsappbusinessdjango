# Generated by Django 2.2.6 on 2019-11-23 05:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('messageprocess', '0019_auto_20191123_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageprocessmodel',
            name='message_uuid',
            field=models.TextField(default=uuid.UUID('3c291762-0db2-11ea-a911-645a049d591d')),
        ),
    ]
