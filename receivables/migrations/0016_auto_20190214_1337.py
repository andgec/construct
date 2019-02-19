# Generated by Django 2.1.4 on 2019-02-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receivables', '0015_auto_20190122_1708'),
    ]
    operations = [
        migrations.AddField(
            model_name='project',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='project',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='Visible'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]