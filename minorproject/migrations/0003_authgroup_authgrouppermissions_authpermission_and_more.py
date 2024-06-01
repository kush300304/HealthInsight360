# Generated by Django 5.0.4 on 2024-04-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minorproject', '0002_allergies_delete_allergy'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('first_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Careplans',
            fields=[
                ('id', models.TextField(db_column='Id', primary_key=True, serialize=False)),
                ('start', models.TextField(blank=True, db_column='START', null=True)),
                ('stop', models.TextField(blank=True, db_column='STOP', null=True)),
                ('patient', models.TextField(blank=True, db_column='PATIENT', null=True)),
                ('encounter', models.TextField(blank=True, db_column='ENCOUNTER', null=True)),
                ('code', models.TextField(blank=True, db_column='CODE', null=True)),
                ('description', models.TextField(blank=True, db_column='DESCRIPTION', null=True)),
                ('reasoncode', models.TextField(blank=True, db_column='REASONCODE', null=True)),
                ('reasondescription', models.TextField(blank=True, db_column='REASONDESCRIPTION', null=True)),
            ],
            options={
                'db_table': 'careplans',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Conditions',
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
                'db_table': 'conditions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TextField(blank=True, db_column='START', null=True)),
                ('stop', models.TextField(blank=True, db_column='STOP', null=True)),
                ('patient', models.TextField(blank=True, db_column='PATIENT', null=True)),
                ('encounter', models.TextField(blank=True, db_column='ENCOUNTER', null=True)),
                ('code', models.TextField(blank=True, db_column='CODE', null=True)),
                ('description', models.TextField(blank=True, db_column='DESCRIPTION', null=True)),
                ('udi', models.TextField(blank=True, db_column='UDI', null=True)),
            ],
            options={
                'db_table': 'devices',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
                ('action_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('gender', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('department', models.CharField(max_length=30)),
                ('specializations', models.CharField(db_column='Specializations', max_length=30)),
                ('phone', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'doctor_doctor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Encounters',
            fields=[
                ('id', models.TextField(db_column='Id', primary_key=True, serialize=False)),
                ('start', models.TextField(blank=True, db_column='START', null=True)),
                ('stop', models.TextField(blank=True, db_column='STOP', null=True)),
                ('patient', models.TextField(blank=True, db_column='PATIENT', null=True)),
                ('organization', models.TextField(blank=True, db_column='ORGANIZATION', null=True)),
                ('provider', models.TextField(blank=True, db_column='PROVIDER', null=True)),
                ('payer', models.TextField(blank=True, db_column='PAYER', null=True)),
                ('encounterclass', models.TextField(blank=True, db_column='ENCOUNTERCLASS', null=True)),
                ('code', models.TextField(blank=True, db_column='CODE', null=True)),
                ('description', models.TextField(blank=True, db_column='DESCRIPTION', null=True)),
                ('base_encounter_cost', models.TextField(blank=True, db_column='BASE_ENCOUNTER_COST', null=True)),
                ('total_claim_cost', models.TextField(blank=True, db_column='TOTAL_CLAIM_COST', null=True)),
                ('payer_coverage', models.TextField(blank=True, db_column='PAYER_COVERAGE', null=True)),
                ('reasoncode', models.TextField(blank=True, db_column='REASONCODE', null=True)),
                ('reasondescription', models.TextField(blank=True, db_column='REASONDESCRIPTION', null=True)),
            ],
            options={
                'db_table': 'encounters',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ImagingStudies',
            fields=[
                ('id', models.TextField(db_column='Id', primary_key=True, serialize=False)),
                ('date', models.TextField(blank=True, db_column='DATE', null=True)),
                ('patient', models.TextField(blank=True, db_column='PATIENT', null=True)),
                ('encounter', models.TextField(blank=True, db_column='ENCOUNTER', null=True)),
                ('bodysite_code', models.TextField(blank=True, db_column='BODYSITE_CODE', null=True)),
                ('bodysite_description', models.TextField(blank=True, db_column='BODYSITE_DESCRIPTION', null=True)),
                ('modality_code', models.TextField(blank=True, db_column='MODALITY_CODE', null=True)),
                ('modality_description', models.TextField(blank=True, db_column='MODALITY_DESCRIPTION', null=True)),
                ('sop_code', models.TextField(blank=True, db_column='SOP_CODE', null=True)),
                ('sop_description', models.TextField(blank=True, db_column='SOP_DESCRIPTION', null=True)),
            ],
            options={
                'db_table': 'imaging_studies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Immunizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(blank=True, db_column='DATE', null=True)),
                ('patient', models.TextField(blank=True, db_column='PATIENT', null=True)),
                ('encounter', models.TextField(blank=True, db_column='ENCOUNTER', null=True)),
                ('code', models.TextField(blank=True, db_column='CODE', null=True)),
                ('description', models.TextField(blank=True, db_column='DESCRIPTION', null=True)),
                ('base_cost', models.TextField(blank=True, db_column='BASE_COST', null=True)),
            ],
            options={
                'db_table': 'immunizations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TextField(blank=True, db_column='START', null=True)),
                ('stop', models.TextField(blank=True, db_column='STOP', null=True)),
                ('patient', models.TextField(blank=True, db_column='PATIENT', null=True)),
                ('payer', models.TextField(blank=True, db_column='PAYER', null=True)),
                ('encounter', models.TextField(blank=True, db_column='ENCOUNTER', null=True)),
                ('code', models.TextField(blank=True, db_column='CODE', null=True)),
                ('description', models.TextField(blank=True, db_column='DESCRIPTION', null=True)),
                ('base_cost', models.TextField(blank=True, db_column='BASE_COST', null=True)),
                ('payer_coverage', models.TextField(blank=True, db_column='PAYER_COVERAGE', null=True)),
                ('dispenses', models.TextField(blank=True, db_column='DISPENSES', null=True)),
                ('totalcost', models.TextField(blank=True, db_column='TOTALCOST', null=True)),
                ('reasoncode', models.TextField(blank=True, db_column='REASONCODE', null=True)),
                ('reasondescription', models.TextField(blank=True, db_column='REASONDESCRIPTION', null=True)),
            ],
            options={
                'db_table': 'medications',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Observations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(blank=True, db_column='DATE', null=True)),
                ('patient', models.TextField(blank=True, db_column='PATIENT', null=True)),
                ('encounter', models.TextField(blank=True, db_column='ENCOUNTER', null=True)),
                ('code', models.TextField(blank=True, db_column='CODE', null=True)),
                ('description', models.TextField(blank=True, db_column='DESCRIPTION', null=True)),
                ('value', models.TextField(blank=True, db_column='VALUE', null=True)),
                ('units', models.TextField(blank=True, db_column='UNITS', null=True)),
                ('type', models.TextField(blank=True, db_column='TYPE', null=True)),
            ],
            options={
                'db_table': 'observations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.TextField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='NAME', null=True)),
                ('address', models.TextField(blank=True, db_column='ADDRESS', null=True)),
                ('city', models.TextField(blank=True, db_column='CITY', null=True)),
                ('state', models.TextField(blank=True, db_column='STATE', null=True)),
                ('zip', models.TextField(blank=True, db_column='ZIP', null=True)),
                ('lat', models.TextField(blank=True, db_column='LAT', null=True)),
                ('lon', models.TextField(blank=True, db_column='LON', null=True)),
                ('phone', models.TextField(blank=True, db_column='PHONE', null=True)),
                ('revenue', models.TextField(blank=True, db_column='REVENUE', null=True)),
                ('utilization', models.TextField(blank=True, db_column='UTILIZATION', null=True)),
            ],
            options={
                'db_table': 'organizations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('gender', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('blood', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'patient_patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.TextField(db_column='Id', primary_key=True, serialize=False)),
                ('birthdate', models.TextField(blank=True, db_column='BIRTHDATE', null=True)),
                ('deathdate', models.TextField(blank=True, db_column='DEATHDATE', null=True)),
                ('ssn', models.TextField(blank=True, db_column='SSN', null=True)),
                ('drivers', models.TextField(blank=True, db_column='DRIVERS', null=True)),
                ('passport', models.TextField(blank=True, db_column='PASSPORT', null=True)),
                ('prefix', models.TextField(blank=True, db_column='PREFIX', null=True)),
                ('first', models.TextField(blank=True, db_column='FIRST', null=True)),
                ('last', models.TextField(blank=True, db_column='LAST', null=True)),
                ('suffix', models.TextField(blank=True, db_column='SUFFIX', null=True)),
                ('maiden', models.TextField(blank=True, db_column='MAIDEN', null=True)),
                ('marital', models.TextField(blank=True, db_column='MARITAL', null=True)),
                ('race', models.TextField(blank=True, db_column='RACE', null=True)),
                ('ethnicity', models.TextField(blank=True, db_column='ETHNICITY', null=True)),
                ('gender', models.TextField(blank=True, db_column='GENDER', null=True)),
                ('birthplace', models.TextField(blank=True, db_column='BIRTHPLACE', null=True)),
                ('address', models.TextField(blank=True, db_column='ADDRESS', null=True)),
                ('city', models.TextField(blank=True, db_column='CITY', null=True)),
                ('state', models.TextField(blank=True, db_column='STATE', null=True)),
                ('county', models.TextField(blank=True, db_column='COUNTY', null=True)),
                ('zip', models.TextField(blank=True, db_column='ZIP', null=True)),
                ('lat', models.TextField(blank=True, db_column='LAT', null=True)),
                ('lon', models.TextField(blank=True, db_column='LON', null=True)),
                ('healthcare_expenses', models.TextField(blank=True, db_column='HEALTHCARE_EXPENSES', null=True)),
                ('healthcare_coverage', models.TextField(blank=True, db_column='HEALTHCARE_COVERAGE', null=True)),
            ],
            options={
                'db_table': 'patients',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payers',
            fields=[
                ('id', models.TextField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='NAME', null=True)),
                ('address', models.TextField(blank=True, db_column='ADDRESS', null=True)),
                ('city', models.TextField(blank=True, db_column='CITY', null=True)),
                ('state_headquartered', models.TextField(blank=True, db_column='STATE_HEADQUARTERED', null=True)),
                ('zip', models.TextField(blank=True, db_column='ZIP', null=True)),
                ('phone', models.TextField(blank=True, db_column='PHONE', null=True)),
                ('amount_covered', models.TextField(blank=True, db_column='AMOUNT_COVERED', null=True)),
                ('amount_uncovered', models.TextField(blank=True, db_column='AMOUNT_UNCOVERED', null=True)),
                ('revenue', models.TextField(blank=True, db_column='REVENUE', null=True)),
                ('covered_encounters', models.TextField(blank=True, db_column='COVERED_ENCOUNTERS', null=True)),
                ('uncovered_encounters', models.TextField(blank=True, db_column='UNCOVERED_ENCOUNTERS', null=True)),
                ('covered_medications', models.TextField(blank=True, db_column='COVERED_MEDICATIONS', null=True)),
                ('uncovered_medications', models.TextField(blank=True, db_column='UNCOVERED_MEDICATIONS', null=True)),
                ('covered_procedures', models.TextField(blank=True, db_column='COVERED_PROCEDURES', null=True)),
                ('uncovered_procedures', models.TextField(blank=True, db_column='UNCOVERED_PROCEDURES', null=True)),
                ('covered_immunizations', models.TextField(blank=True, db_column='COVERED_IMMUNIZATIONS', null=True)),
                ('uncovered_immunizations', models.TextField(blank=True, db_column='UNCOVERED_IMMUNIZATIONS', null=True)),
                ('unique_customers', models.TextField(blank=True, db_column='UNIQUE_CUSTOMERS', null=True)),
                ('qols_avg', models.TextField(blank=True, db_column='QOLS_AVG', null=True)),
                ('member_months', models.TextField(blank=True, db_column='MEMBER_MONTHS', null=True)),
            ],
            options={
                'db_table': 'payers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PayerTransitions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.TextField(blank=True, db_column='PATIENT', null=True)),
                ('start_year', models.TextField(blank=True, db_column='START_YEAR', null=True)),
                ('end_year', models.TextField(blank=True, db_column='END_YEAR', null=True)),
                ('payer', models.TextField(blank=True, db_column='PAYER', null=True)),
                ('ownership', models.TextField(blank=True, db_column='OWNERSHIP', null=True)),
            ],
            options={
                'db_table': 'payer_transitions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Procedures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(blank=True, db_column='DATE', null=True)),
                ('patient', models.TextField(blank=True, db_column='PATIENT', null=True)),
                ('encounter', models.TextField(blank=True, db_column='ENCOUNTER', null=True)),
                ('code', models.TextField(blank=True, db_column='CODE', null=True)),
                ('description', models.TextField(blank=True, db_column='DESCRIPTION', null=True)),
                ('base_cost', models.TextField(blank=True, db_column='BASE_COST', null=True)),
                ('reasoncode', models.TextField(blank=True, db_column='REASONCODE', null=True)),
                ('reasondescription', models.TextField(blank=True, db_column='REASONDESCRIPTION', null=True)),
            ],
            options={
                'db_table': 'procedures',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('id', models.TextField(db_column='Id', primary_key=True, serialize=False)),
                ('organization', models.TextField(blank=True, db_column='ORGANIZATION', null=True)),
                ('name', models.TextField(blank=True, db_column='NAME', null=True)),
                ('gender', models.TextField(blank=True, db_column='GENDER', null=True)),
                ('speciality', models.TextField(blank=True, db_column='SPECIALITY', null=True)),
                ('address', models.TextField(blank=True, db_column='ADDRESS', null=True)),
                ('city', models.TextField(blank=True, db_column='CITY', null=True)),
                ('state', models.TextField(blank=True, db_column='STATE', null=True)),
                ('zip', models.TextField(blank=True, db_column='ZIP', null=True)),
                ('lat', models.TextField(blank=True, db_column='LAT', null=True)),
                ('lon', models.TextField(blank=True, db_column='LON', null=True)),
                ('utilization', models.TextField(blank=True, db_column='UTILIZATION', null=True)),
            ],
            options={
                'db_table': 'providers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Supplies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(blank=True, db_column='DATE', null=True)),
                ('patient', models.TextField(blank=True, db_column='PATIENT', null=True)),
                ('encounter', models.TextField(blank=True, db_column='ENCOUNTER', null=True)),
                ('code', models.TextField(blank=True, db_column='CODE', null=True)),
                ('description', models.TextField(blank=True, db_column='DESCRIPTION', null=True)),
                ('quantity', models.TextField(blank=True, db_column='QUANTITY', null=True)),
            ],
            options={
                'db_table': 'supplies',
                'managed': False,
            },
        ),
    ]