# Generated by Django 2.2.1 on 2019-08-20 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0012_auto_20190711_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, default='', max_length=100)),
                ('dtm', models.DateTimeField()),
            ],
        ),
    ]