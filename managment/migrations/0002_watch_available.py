# Generated by Django 3.2 on 2021-04-24 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='available',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
