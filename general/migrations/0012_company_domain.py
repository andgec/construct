# Generated by Django 2.2.9 on 2020-02-24 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0011_auto_20200214_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='domain',
            field=models.CharField(max_length=150, null=True, verbose_name='domain'),
        ),
    ]
