# Generated by Django 2.2.6 on 2019-11-27 18:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanagement', '0012_auto_20191125_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediamessagemodel',
            name='uuid',
            field=models.TextField(default=uuid.UUID('2ec6f086-1141-11ea-8e94-645a049d591d')),
        ),
    ]