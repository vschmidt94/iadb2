# Generated by Django 2.0 on 2018-01-19 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requirements', '0006_auto_20180114_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_identifier', models.CharField(help_text="ACME Co.'s internal\n                                       identification number for the Document.", max_length=20, unique=True, verbose_name='Document ID')),
                ('doc_title', models.CharField(help_text='The Document Title or a brief description.', max_length=128, verbose_name='Title')),
                ('note', models.TextField(blank=True, help_text='Auditor-to-Auditor internal note(s) that\n                            convey additional information which may be useful or good to\n                            know.', null=True, verbose_name='Note')),
                ('is_active', models.BooleanField(default=True, help_text='Is the Document considered active or retired?', verbose_name='Active')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('created_by_userid', models.CharField(max_length=20, verbose_name='Created by')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'ordering': ['doc_identifier'],
            },
        ),
        migrations.AlterField(
            model_name='requirement',
            name='coverage_by',
            field=models.CharField(choices=[('S', 'Self'), ('P', 'Parent'), ('C', 'Child(ren)'), ('NA', 'N/A')], default='S', help_text="Covered by. Choices are:\n                                                SELF = This requirement is a\n                                                coverage point.  PARENT = This\n                                                requirment inherits the parent's coverage,\n                                                typically used for standard clauses which\n                                                end up being long lists and thus don't\n                                                warrant individual questions.  CHILD(REN) =\n                                                this requirement delegates\n                                                coverage to child(ren) requirements.\n                                                Typically used for 'placeholder' requriements,\n                                                such as section headers.", max_length=2, verbose_name='Coverage By'),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='is_active',
            field=models.BooleanField(default='True', help_text='Is requirement active? Only active\n                                                 Requirements will be considered in\n                                                 coverage logic.', verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='note',
            field=models.TextField(blank=True, help_text='Auditor-to-Auditor note(s) that convey additional\n                                         information that may be useful.\n\n                                         Often explains delegation of coverage.', max_length=500, null=True, verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='parent',
            field=models.ForeignKey(blank='True', help_text='The Parent requirement (if any) of this\n                                            requirement. Used in conjunction with\n                                            COVERAGE (above) to determine coverage\n                                             obligations.', null='True', on_delete='Protect', related_name='children', to='requirements.Requirement', verbose_name='Parent'),
        ),
        migrations.AlterField(
            model_name='standard',
            name='date_inactive',
            field=models.DateField(blank='True', help_text='Date the Standard was retired from audit\n                            purposes.', null='True', verbose_name='Date Retired'),
        ),
        migrations.AlterField(
            model_name='standard',
            name='revision',
            field=models.CharField(help_text='Identifier for the exact version of the\n                                Standards being used.', max_length=5, verbose_name='Revision'),
        ),
    ]
