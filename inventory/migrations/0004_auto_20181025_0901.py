# Generated by Django 2.1.1 on 2018-10-25 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20181024_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', max_length=250, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Item Translation',
                'db_table': 'inventory_item_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
            },
        ),
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.RemoveField(
            model_name='item',
            name='name',
        ),
        migrations.AddField(
            model_name='itemtranslation',
            name='master',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='inventory.Item'),
        ),
        migrations.AlterUniqueTogether(
            name='itemtranslation',
            unique_together={('language_code', 'master')},
        ),
    ]
