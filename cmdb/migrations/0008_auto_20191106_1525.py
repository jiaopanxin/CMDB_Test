# Generated by Django 2.1.5 on 2019-11-06 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0007_auto_20191106_1446'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variable',
            options={'verbose_name': '变量表', 'verbose_name_plural': '变量表'},
        ),
        migrations.RemoveField(
            model_name='variable',
            name='group',
        ),
        migrations.RemoveField(
            model_name='variable',
            name='host',
        ),
    ]
