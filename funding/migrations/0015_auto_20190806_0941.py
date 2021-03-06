# Generated by Django 2.1.4 on 2019-08-06 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0014_merge_20190730_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundingsource',
            name='pi_email',
            field=models.EmailField(help_text='Please note that the PI will be notified with the email address provided, and asked to attribute the funds to SCW.', max_length=254, null=True, verbose_name='PI Email'),
        ),
        migrations.AlterField(
            model_name='historicalfundingsource',
            name='pi_email',
            field=models.EmailField(help_text='Please note that the PI will be notified with the email address provided, and asked to attribute the funds to SCW.', max_length=254, null=True, verbose_name='PI Email'),
        ),
    ]
