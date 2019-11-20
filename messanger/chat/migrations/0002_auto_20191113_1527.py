# Generated by Django 2.2.5 on 2019-11-13 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attachment',
            name='chat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chat.Chat'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chat.Message'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]