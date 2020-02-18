# Generated by Django 2.2.9 on 2020-01-27 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0010_unitofmeasure_company'),
        ('receivables', '0017_auto_20200117_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='general.Company'),
        ),
        migrations.AddField(
            model_name='project',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='general.Company'),
        ),
        migrations.AddField(
            model_name='projectcategory',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='general.Company'),
        ),
        migrations.AddField(
            model_name='salesorderheader',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='general.Company'),
        ),
        migrations.AddField(
            model_name='salesorderline',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='general.Company'),
        ),
        migrations.AddField(
            model_name='worktimejournal',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='general.Company'),
        ),
    ]