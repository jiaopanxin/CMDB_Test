# Generated by Django 2.1.5 on 2019-11-06 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0005_variable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variable',
            name='host',
            field=models.ManyToManyField(blank=True, null=True, related_name='variable', to='cmdb.Server', verbose_name='所属主机'),
        ),
    ]
