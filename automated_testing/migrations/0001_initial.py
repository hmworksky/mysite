# Generated by Django 2.0.4 on 2018-05-10 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('interface_control', '0002_auto_20180510_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterfaceAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='string', max_length=50)),
                ('min', models.CharField(default=0, max_length=50, null=True)),
                ('max', models.CharField(default=0, max_length=50, null=True)),
                ('field', models.CharField(max_length=50, verbose_name='字段名')),
                ('is_null', models.CharField(default=0, max_length=500, verbose_name='非空标识')),
                ('memo', models.CharField(default=0, max_length=500, null=True, verbose_name='描述')),
                ('interface', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='interface_control.InterfaceInfo')),
            ],
        ),
        migrations.CreateModel(
            name='InterfaceConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(null=True, unique=True)),
                ('status', models.IntegerField(default=1)),
                ('remark', models.CharField(max_length=500)),
            ],
        ),
    ]
