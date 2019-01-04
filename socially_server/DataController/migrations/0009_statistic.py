# Generated by Django 2.1.3 on 2019-01-01 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataController', '0008_auto_20181231_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=20)),
                ('thing', models.CharField(default='', max_length=20)),
                ('place', models.CharField(default='', max_length=20)),
                ('deadDate', models.DateField()),
                ('deadTime', models.TimeField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('number', models.IntegerField()),
                ('eventKey', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataController.User')),
            ],
        ),
    ]