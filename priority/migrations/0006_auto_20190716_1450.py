# Generated by Django 2.2.2 on 2019-07-16 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priority', '0005_auto_20190716_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slurm_priority',
            name='project_code',
            field=models.CharField(max_length=20, verbose_name='SCW Project code extracted from sacct dump'),
        ),
    ]
