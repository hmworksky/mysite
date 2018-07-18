# Generated by Django 2.0.4 on 2018-05-14 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automated_testing', '0002_auto_20180510_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(max_length=50, verbose_name='用例名，即函数名')),
                ('case_memo', models.CharField(max_length=50, verbose_name='用例描述')),
                ('class_name', models.CharField(max_length=50, verbose_name='类名')),
                ('class_memo', models.CharField(max_length=50, verbose_name='类的描述')),
            ],
        ),
        migrations.CreateModel(
            name='GameInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='游戏名')),
                ('memo', models.CharField(max_length=50, verbose_name='游戏描述')),
            ],
        ),
        migrations.AddField(
            model_name='caseinfo',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='automated_testing.GameInfo'),
        ),
        migrations.AlterUniqueTogether(
            name='caseinfo',
            unique_together={('class_name', 'case_name')},
        ),
    ]