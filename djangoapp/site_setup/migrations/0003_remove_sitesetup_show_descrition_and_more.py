# Generated by Django 4.2.3 on 2023-07-22 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0002_sitesetup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesetup',
            name='show_descrition',
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='show_description',
            field=models.BooleanField(default=True),
        ),
    ]