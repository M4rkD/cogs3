# Generated by Django 2.0.2 on 2018-09-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0016_institution_funding_document_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='funding_document_receiver',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='funding_document_template',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
