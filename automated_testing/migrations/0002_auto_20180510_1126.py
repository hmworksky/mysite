# Generated by Django 2.0.4 on 2018-05-10 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interface_control', '0002_auto_20180510_1024'),
        ('automated_testing', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='interfaceattr',
            unique_together={('interface', 'field')},
        ),
    ]
