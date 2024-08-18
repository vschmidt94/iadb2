# Generated by Django 2.0 on 2018-01-06 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=50, unique=True, verbose_name='Department')),
            ],
            options={
                'verbose_name_plural': 'Departments',
                'ordering': ['dept_name'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_first', models.CharField(max_length=50, verbose_name='First Name')),
                ('name_last', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_name', models.CharField(max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active Flag')),
                ('iadb1_id', models.PositiveIntegerField(default=None, null=True, verbose_name='IADB1 id')),
                ('created_by_userid', models.CharField(max_length=50, verbose_name='Created by user')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('dept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.Department')),
            ],
            options={
                'verbose_name_plural': 'People',
                'ordering': ['name_last', 'name_first'],
            },
        ),
    ]
