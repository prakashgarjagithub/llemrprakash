# Generated by Django 3.0.5 on 2020-09-24 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workup', '0004_auto_20200921_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalworkup',
            name='pmh_psh',
            field=models.TextField(blank=True, db_column='old_pmh_psh', verbose_name='PMH/PSH'),
        ),
        migrations.AlterField(
            model_name='workup',
            name='pmh_psh',
            field=models.TextField(blank=True, db_column='old_pmh_psh', verbose_name='PMH/PSH'),
        ),
    ]
