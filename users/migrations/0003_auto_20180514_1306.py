# Generated by Django 2.0.2 on 2018-05-14 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_project_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name_plural': 'Users'},
        ),
    ]