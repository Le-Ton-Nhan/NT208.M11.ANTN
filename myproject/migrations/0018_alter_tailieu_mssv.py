# Generated by Django 3.2.8 on 2021-11-07 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0017_auto_20211107_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tailieu',
            name='MSSV',
            field=models.CharField(max_length=20),
        ),
    ]
