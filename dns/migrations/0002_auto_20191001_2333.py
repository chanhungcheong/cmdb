# Generated by Django 2.2.5 on 2019-10-01 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='record_value',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='记录值'),
        ),
    ]
