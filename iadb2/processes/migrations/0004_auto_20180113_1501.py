# Generated by Django 2.0 on 2018-01-13 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0003_auto_20180106_0824'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='process',
            options={'ordering': ['name'], 'verbose_name': 'Process', 'verbose_name_plural': 'Processes'},
        ),
        migrations.AlterField(
            model_name='process',
            name='frequency',
            field=models.PositiveSmallIntegerField(default=1, help_text='How many times per year the Process\n                                                  should be audited. ( 1 for yearly, 4 for \n                                                  quarterly ).', verbose_name='Frequency'),
        ),
        migrations.AlterField(
            model_name='process',
            name='iadb1_id',
            field=models.PositiveIntegerField(default=None, help_text='UID of Process in iadb1. Used for data\n                                           migration.', null=True, verbose_name='IADB1 ID#'),
        ),
        migrations.AlterField(
            model_name='process',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Is this Process current in-use. Inactive\n                                     Processes will NOT be included in audit processing.', verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='process',
            name='name',
            field=models.CharField(help_text='Descriptive name for the process area.', max_length=50, unique=True, verbose_name='Process Name'),
        ),
        migrations.AlterField(
            model_name='process',
            name='notes',
            field=models.TextField(blank=True, help_text='Any notes or commentary for the Process. Generally\n                              auditor-to-auditor, for reference only.', max_length=500, verbose_name='Note(s)'),
        ),
    ]
