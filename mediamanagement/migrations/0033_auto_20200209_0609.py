# Generated by Django 2.2.6 on 2020-02-09 00:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanagement', '0032_auto_20200209_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediamessagemodel',
            name='uuid',
            field=models.TextField(default=uuid.UUID('87fa52de-4ad4-11ea-8c72-645a049d591d')),
        ),
    ]