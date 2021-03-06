# Generated by Django 2.2.7 on 2019-11-20 12:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('messageprocess', '0015_auto_20191120_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='readcsvfilemodel',
            name='body',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='readcsvfilemodel',
            name='phone',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='messageprocessmodel',
            name='message_uuid',
            field=models.TextField(default=uuid.UUID('9365a1b8-0b8d-11ea-a0cc-c42c03361ed0')),
        ),
    ]
