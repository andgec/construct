# Generated by Django 2.1.1 on 2018-09-13 13:32

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('address2', models.CharField(blank=True, default='', max_length=100)),
                ('city', models.CharField(blank=True, default='', max_length=60)),
                ('post_code', models.CharField(blank=True, default='', max_length=16)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('email', models.EmailField(blank=True, default='', max_length=120)),
                ('phone_no', models.CharField(blank=True, default='', max_length=20)),
                ('mobile_no', models.CharField(blank=True, default='', max_length=20)),
                ('fax_no', models.CharField(blank=True, default='', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('address2', models.CharField(blank=True, default='', max_length=100)),
                ('city', models.CharField(blank=True, default='', max_length=60)),
                ('post_code', models.CharField(blank=True, default='', max_length=16)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('email', models.EmailField(blank=True, default='', max_length=120)),
                ('phone_no', models.CharField(blank=True, default='', max_length=20)),
                ('mobile_no', models.CharField(blank=True, default='', max_length=20)),
                ('fax_no', models.CharField(blank=True, default='', max_length=20)),
                ('name', models.CharField(max_length=60, unique=True)),
                ('number', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('address2', models.CharField(blank=True, default='', max_length=100)),
                ('city', models.CharField(blank=True, default='', max_length=60)),
                ('post_code', models.CharField(blank=True, default='', max_length=16)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('email', models.EmailField(blank=True, default='', max_length=120)),
                ('phone_no', models.CharField(blank=True, default='', max_length=20)),
                ('mobile_no', models.CharField(blank=True, default='', max_length=20)),
                ('fax_no', models.CharField(blank=True, default='', max_length=20)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(blank=True, default='', max_length=60)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Company')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
