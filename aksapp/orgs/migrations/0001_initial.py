# Generated by Django 2.0.7 on 2018-07-11 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('entry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orgs.Entry')),
                ('record', models.IntegerField()),
            ],
            bases=('orgs.entry',),
        ),
    ]
