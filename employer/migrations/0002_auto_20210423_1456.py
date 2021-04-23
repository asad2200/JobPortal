# Generated by Django 3.2 on 2021-04-23 09:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AddField(
            model_name='job',
            name='profile',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
