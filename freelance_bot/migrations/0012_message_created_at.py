# Generated by Django 3.2 on 2023-02-27 13:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('freelance_bot', '0011_auto_20230227_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Время и дата сообщения'),
        ),
    ]
