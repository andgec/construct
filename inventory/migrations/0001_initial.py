# Generated by Django 2.1.1 on 2018-09-21 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general', '0004_unitofmeasure'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('active', models.BooleanField(default=True)),
                ('price', models.DecimalField(blank=True, decimal_places=4, max_digits=14)),
            ],
        ),
        migrations.CreateModel(
            name='ItemGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='item_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.ItemGroup'),
        ),
        migrations.AddField(
            model_name='item',
            name='unit_of_measure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='general.UnitOfMeasure'),
        ),
    ]
