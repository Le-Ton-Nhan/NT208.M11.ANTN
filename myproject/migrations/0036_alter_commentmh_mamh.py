# Generated by Django 3.2.8 on 2021-11-14 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0035_auto_20211113_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmh',
            name='MaMH',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myproject.monhoc'),
        ),
    ]
