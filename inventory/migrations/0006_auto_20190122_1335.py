# Generated by Django 2.1.4 on 2019-01-22 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20181031_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='inventory.ItemGroup', verbose_name='Item group'),
        ),
    ]