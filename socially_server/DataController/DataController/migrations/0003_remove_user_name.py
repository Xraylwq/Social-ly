# Generated by Django 2.1.3 on 2018-12-25 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DataController', '0002_auto_20181218_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
