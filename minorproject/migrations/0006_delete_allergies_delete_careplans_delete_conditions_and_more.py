# Generated by Django 5.0.4 on 2024-05-01 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minorproject', '0005_allergies'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Allergies',
        ),
        migrations.DeleteModel(
            name='Careplans',
        ),
        migrations.DeleteModel(
            name='Conditions',
        ),
        migrations.DeleteModel(
            name='Devices',
        ),
        migrations.DeleteModel(
            name='Encounters',
        ),
        migrations.DeleteModel(
            name='ImagingStudies',
        ),
        migrations.DeleteModel(
            name='Immunizations',
        ),
        migrations.DeleteModel(
            name='Medications',
        ),
        migrations.DeleteModel(
            name='Observations',
        ),
        migrations.DeleteModel(
            name='Payers',
        ),
        migrations.DeleteModel(
            name='PayerTransitions',
        ),
        migrations.DeleteModel(
            name='Procedures',
        ),
        migrations.DeleteModel(
            name='Providers',
        ),
        migrations.DeleteModel(
            name='Supplies',
        ),
    ]
