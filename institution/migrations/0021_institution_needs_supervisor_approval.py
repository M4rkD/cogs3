# Generated by Django 2.0.2 on 2018-09-21 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0020_auto_20180919_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='needs_supervisor_approval',
            field=models.BooleanField(default=False),
        ),
    ]
