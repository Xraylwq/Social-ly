# Generated by Django 2.1.3 on 2018-12-09 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataController', '0002_auto_20181202_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('time', models.TimeField(default='', verbose_name='time')),
                ('info', models.CharField(default='', max_length=40, verbose_name='info')),
                ('type', models.IntegerField(verbose_name='type')),
                ('invitee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invitee', to='DataController.User')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataController.User')),
            ],
            options={
                'verbose_name': 'Invitation',
            },
        ),
        migrations.AddField(
            model_name='calendar',
            name='type',
            field=models.IntegerField(default=1, verbose_name='type'),
        ),
    ]