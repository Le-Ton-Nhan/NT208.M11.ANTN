# Generated by Django 3.2.8 on 2021-11-07 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0024_auto_20211107_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='MaTL',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myproject.tailieu'),
        ),
    ]
