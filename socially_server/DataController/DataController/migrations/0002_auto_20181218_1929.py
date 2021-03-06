# Generated by Django 2.1.3 on 2018-12-18 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataController', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='inviter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inviter', to='DataController.User'),
        ),
    ]
