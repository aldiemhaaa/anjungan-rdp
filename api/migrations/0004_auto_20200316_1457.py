# Generated by Django 3.0.2 on 2020-03-16 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200316_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nosep',
            name='noSep',
            field=models.CharField(default='', max_length=19),
        ),
    ]