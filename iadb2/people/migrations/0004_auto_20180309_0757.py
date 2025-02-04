# Generated by Django 2.0 on 2018-03-09 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20180302_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created_by_userid',
            field=models.CharField(default='iadb_sys', max_length=12, verbose_name='Created By'),
        ),
        migrations.AlterField(
            model_name='person',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date Created`'),
        ),
        migrations.AlterField(
            model_name='person',
            name='dept',
            field=models.ForeignKey(blank=True, help_text='(Optional) The department / work area for a user.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.Department', verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='person',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Is this an active person record?', verbose_name='Active'),
        ),
    ]
