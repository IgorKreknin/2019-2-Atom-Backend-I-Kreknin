# Generated by Django 2.2.5 on 2019-11-20 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20191120_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.TextField(default='http://example.com/img', null=True),
        ),
    ]