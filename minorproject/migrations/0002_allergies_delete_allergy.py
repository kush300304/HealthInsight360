# Generated by Django 5.0.4 on 2024-04-22 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minorproject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TextField(blank=True, db_column='START', null=True)),
                ('stop', models.TextField(blank=True, db_column='STOP', null=True)),
                ('patient', models.TextField(blank=True, db_column='PATIENT', null=True)),
                ('encounter', models.TextField(blank=True, db_column='ENCOUNTER', null=True)),
                ('code', models.TextField(blank=True, db_column='CODE', null=True)),
                ('description', models.TextField(blank=True, db_column='DESCRIPTION', null=True)),
            ],
            options={
                'db_table': 'allergies',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Allergy',
        ),
    ]