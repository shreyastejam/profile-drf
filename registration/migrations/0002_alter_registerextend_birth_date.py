# Generated by Django 3.2.4 on 2021-07-08 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerextend',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
