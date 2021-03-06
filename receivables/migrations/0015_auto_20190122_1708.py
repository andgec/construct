# Generated by Django 2.1.4 on 2019-01-22 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receivables', '0014_auto_20181114_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='worktimejournal',
            name='overtime_100',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Overtime 100%'),
        ),
        migrations.AddField(
            model_name='worktimejournal',
            name='overtime_50',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Overtime 50%'),
        ),
    ]
