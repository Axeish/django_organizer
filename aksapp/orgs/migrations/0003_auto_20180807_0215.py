# Generated by Django 2.0.7 on 2018-08-07 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0002_auto_20180720_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('record', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('done', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('done', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orgs.Task'),
        ),
    ]