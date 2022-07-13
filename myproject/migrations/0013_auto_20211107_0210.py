# Generated by Django 3.2.8 on 2021-11-06 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0012_merge_20211107_0206'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Toan_Tin_KHTN',
        ),
        migrations.RemoveField(
            model_name='tailieu',
            name='Path',
        ),
        migrations.RemoveField(
            model_name='tailieu',
            name='date',
        ),
        migrations.AddField(
            model_name='tailieu',
            name='KiemDuyet',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commentmh',
            name='MaMH',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myproject.monhoc'),
        ),
    ]