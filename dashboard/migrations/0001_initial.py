# Generated by Django 3.2 on 2021-04-22 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('role', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
