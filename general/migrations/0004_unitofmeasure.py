# Generated by Django 2.1.1 on 2018-09-21 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_auto_20180914_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitOfMeasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=60)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Units of measure',
            },
        ),
    ]
