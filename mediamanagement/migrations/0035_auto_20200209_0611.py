# Generated by Django 2.2.6 on 2020-02-09 00:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanagement', '0034_auto_20200209_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediamessagemodel',
            name='uuid',
            field=models.TextField(default=uuid.UUID('e1e18562-4ad4-11ea-9937-645a049d591d')),
        ),
    ]