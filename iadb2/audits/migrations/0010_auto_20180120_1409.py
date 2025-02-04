# Generated by Django 2.0 on 2018-01-20 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audits', '0009_auto_20180120_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audittemplate',
            name='for_process',
            field=models.ForeignKey(help_text='The Process this Audit is defined for.', on_delete='Protect', related_name='audit_master_template', to='processes.Process', verbose_name='Process To Audit'),
        ),
    ]
