# Generated by Django 2.2.5 on 2019-11-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20191120_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='BooleanField',
            field=models.BooleanField(default=False),
        ),
    ]