# Generated by Django 2.2.6 on 2019-12-01 05:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('messageprocess', '0030_auto_20191201_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageprocessmodel',
            name='message_uuid',
            field=models.TextField(default=uuid.UUID('3df850dc-13fe-11ea-a0eb-645a049d591d')),
        ),
    ]