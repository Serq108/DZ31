# Generated by Django 2.2.1 on 2019-08-27 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0024_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]