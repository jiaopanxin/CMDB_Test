# Generated by Django 2.1.5 on 2019-11-09 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0011_auto_20191108_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variable2group2server',
            name='variable_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variable_name', to='cmdb.Variable', verbose_name='变量'),
        ),
    ]