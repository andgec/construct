# Generated by Django 2.2.9 on 2020-02-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0013_auto_20200224_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='domain',
            field=models.CharField(max_length=150, unique=True, verbose_name='domain'),
        ),
    ]
