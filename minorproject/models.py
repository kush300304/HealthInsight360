# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Allergies(models.Model):
    start = models.TextField(db_column='START', blank=True, null=True)  # Field name made lowercase.
    stop = models.TextField(db_column='STOP', blank=True, null=True)  # Field name made lowercase.
    patient = models.TextField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    encounter = models.TextField(db_column='ENCOUNTER', blank=True, null=True)  # Field name made lowercase.
    code = models.FloatField(db_column='CODE', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    xid = models.IntegerField(db_column='XID',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '`allergies`'


class Careplans(models.Model):
    id = models.TextField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    start = models.TextField(db_column='START', blank=True, null=True)  # Field name made lowercase.
    stop = models.TextField(db_column='STOP', blank=True, null=True)  # Field name made lowercase.
    patient = models.TextField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    encounter = models.TextField(db_column='ENCOUNTER', blank=True, null=True)  # Field name made lowercase.
    code = models.FloatField(db_column='CODE', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    reasoncode = models.FloatField(db_column='REASONCODE', blank=True, null=True)  # Field name made lowercase.
    reasondescription = models.TextField(db_column='REASONDESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    xid = models.IntegerField(db_column='XID',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '`careplans`'


class Conditions(models.Model):
    start = models.TextField(db_column='START', blank=True, null=True)  # Field name made lowercase.
    stop = models.TextField(db_column='STOP', blank=True, null=True)  # Field name made lowercase.
    patient = models.TextField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    encounter = models.TextField(db_column='ENCOUNTER', blank=True, null=True)  # Field name made lowercase.
    code = models.FloatField(db_column='CODE', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    xid = models.IntegerField(db_column='XID',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '`conditions`'


class Devices(models.Model):
    start = models.TextField(db_column='START', blank=True, null=True)  # Field name made lowercase.
    stop = models.TextField(db_column='STOP', blank=True, null=True)  # Field name made lowercase.
    patient = models.TextField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    encounter = models.TextField(db_column='ENCOUNTER', blank=True, null=True)  # Field name made lowercase.
    code = models.FloatField(db_column='CODE', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    udi = models.TextField(db_column='UDI', blank=True, null=True)  # Field name made lowercase.
    xid = models.IntegerField(db_column='XID',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '`devices`'


class Encounters(models.Model):
    id = models.TextField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    start = models.TextField(db_column='START', blank=True, null=True)  # Field name made lowercase.
    stop = models.TextField(db_column='STOP', blank=True, null=True)  # Field name made lowercase.
    patient = models.TextField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    organization = models.TextField(db_column='ORGANIZATION', blank=True, null=True)  # Field name made lowercase.
    provider = models.TextField(db_column='PROVIDER', blank=True, null=True)  # Field name made lowercase.
    payer = models.TextField(db_column='PAYER', blank=True, null=True)  # Field name made lowercase.
    encounterclass = models.TextField(db_column='ENCOUNTERCLASS', blank=True, null=True)  # Field name made lowercase.
    code = models.FloatField(db_column='CODE', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    base_encounter_cost = models.FloatField(db_column='BASE_ENCOUNTER_COST', blank=True, null=True)  # Field name made lowercase.
    total_claim_cost = models.FloatField(db_column='TOTAL_CLAIM_COST', blank=True, null=True)  # Field name made lowercase.
    payer_coverage = models.FloatField(db_column='PAYER_COVERAGE', blank=True, null=True)  # Field name made lowercase.
    reasoncode = models.TextField(db_column='REASONCODE', blank=True, null=True)  # Field name made lowercase.
    reasondescription = models.TextField(db_column='REASONDESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    xid = models.IntegerField(db_column='XID',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '`encounters`'


class ImagingStudies(models.Model):
    id = models.TextField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    patient = models.TextField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    encounter = models.TextField(db_column='ENCOUNTER', blank=True, null=True)  # Field name made lowercase.
    bodysite_code = models.FloatField(db_column='BODYSITE_CODE', blank=True, null=True)  # Field name made lowercase.
    bodysite_description = models.TextField(db_column='BODYSITE_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    modality_code = models.TextField(db_column='MODALITY_CODE', blank=True, null=True)  # Field name made lowercase.
    modality_description = models.TextField(db_column='MODALITY_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    sop_code = models.TextField(db_column='SOP_CODE', blank=True, null=True)  # Field name made lowercase.
    sop_description = models.TextField(db_column='SOP_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    xid = models.IntegerField(db_column='XID',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '`imaging_studies`'


class Immunizations(models.Model):
    date = models.TextField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    patient = models.TextField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    encounter = models.TextField(db_column='ENCOUNTER', blank=True, null=True)  # Field name made lowercase.
    code = models.FloatField(db_column='CODE', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    base_cost = models.FloatField(db_column='BASE_COST', blank=True, null=True)  # Field name made lowercase.
    xid = models.IntegerField(db_column='XID',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '`immunizations`'


class Medications(models.Model):
    start = models.TextField(db_column='START', blank=True, null=True)  # Field name made lowercase.
    stop = models.TextField(db_column='STOP', blank=True, null=True)  # Field name made lowercase.
    patient = models.TextField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    payer = models.TextField(db_column='PAYER', blank=True, null=True)  # Field name made lowercase.
    encounter = models.TextField(db_column='ENCOUNTER', blank=True, null=True)  # Field name made lowercase.
    code = models.FloatField(db_column='CODE', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    base_cost = models.FloatField(db_column='BASE_COST', blank=True, null=True)  # Field name made lowercase.
    payer_coverage = models.FloatField(db_column='PAYER_COVERAGE', blank=True, null=True)  # Field name made lowercase.
    dispenses = models.FloatField(db_column='DISPENSES', blank=True, null=True)  # Field name made lowercase.
    totalcost = models.FloatField(db_column='TOTALCOST', blank=True, null=True)  # Field name made lowercase.
    reasoncode = models.TextField(db_column='REASONCODE', blank=True, null=True)  # Field name made lowercase.
    reasondescription = models.TextField(db_column='REASONDESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    xid = models.IntegerField(db_column='XID',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '`medications`'


class Observations(models.Model):
    date = models.TextField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    patient = models.TextField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    encounter = models.TextField(db_column='ENCOUNTER', blank=True, null=True)  # Field name made lowercase.
    code = models.TextField(db_column='CODE', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='VALUE', blank=True, null=True)  # Field name made lowercase.
    units = models.TextField(db_column='UNITS', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    xid = models.IntegerField(db_column='XID',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '`observations`'


class Organizations(models.Model):
    id = models.TextField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='ADDRESS', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='CITY', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    zip = models.TextField(db_column='ZIP', blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='LAT', blank=True, null=True)  # Field name made lowercase.
    lon = models.FloatField(db_column='LON', blank=True, null=True)  # Field name made lowercase.
    phone = models.FloatField(db_column='PHONE', blank=True, null=True)  # Field name made lowercase.
    revenue = models.FloatField(db_column='REVENUE', blank=True, null=True)  # Field name made lowercase.
    utilization = models.FloatField(db_column='UTILIZATION', blank=True, null=True)  # Field name made lowercase.
    xid = models.IntegerField(db_column='XID',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '`organizations`'


class Patients(models.Model):
    id = models.TextField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.TextField(db_column='BIRTHDATE', blank=True, null=True)  # Field name made lowercase.
    deathdate = models.TextField(db_column='DEATHDATE', blank=True, null=True)  # Field name made lowercase.
    ssn = models.TextField(db_column='SSN', blank=True, null=True)  # Field name made lowercase.
    drivers = models.TextField(db_column='DRIVERS', blank=True, null=True)  # Field name made lowercase.
    passport = models.TextField(db_column='PASSPORT', blank=True, null=True)  # Field name made lowercase.
    prefix = models.TextField(db_column='PREFIX', blank=True, null=True)  # Field name made lowercase.
    first = models.TextField(db_column='FIRST', blank=True, null=True)  # Field name made lowercase.
    last = models.TextField(db_column='LAST', blank=True, null=True)  # Field name made lowercase.
    suffix = models.TextField(db_column='SUFFIX', blank=True, null=True)  # Field name made lowercase.
    maiden = models.TextField(db_column='MAIDEN', blank=True, null=True)  # Field name made lowercase.
    marital = models.TextField(db_column='MARITAL', blank=True, null=True)  # Field name made lowercase.
    race = models.TextField(db_column='RACE', blank=True, null=True)  # Field name made lowercase.
    ethnicity = models.TextField(db_column='ETHNICITY', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(db_column='GENDER', blank=True, null=True)  # Field name made lowercase.
    birthplace = models.TextField(db_column='BIRTHPLACE', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='ADDRESS', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='CITY', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    county = models.TextField(db_column='COUNTY', blank=True, null=True)  # Field name made lowercase.
    zip = models.TextField(db_column='ZIP', blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='LAT', blank=True, null=True)  # Field name made lowercase.
    lon = models.FloatField(db_column='LON', blank=True, null=True)  # Field name made lowercase.
    healthcare_expenses = models.FloatField(db_column='HEALTHCARE_EXPENSES', blank=True, null=True)  # Field name made lowercase.
    healthcare_coverage = models.FloatField(db_column='HEALTHCARE_COVERAGE', blank=True, null=True)  # Field name made lowercase.
    xid = models.IntegerField(db_column='XID',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '`patients`'


class PayerTransitions(models.Model):
    patient = models.TextField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    start_year = models.FloatField(db_column='START_YEAR', blank=True, null=True)  # Field name made lowercase.
    end_year = models.FloatField(db_column='END_YEAR', blank=True, null=True)  # Field name made lowercase.
    payer = models.TextField(db_column='PAYER', blank=True, null=True)  # Field name made lowercase.
    ownership = models.TextField(db_column='OWNERSHIP', blank=True, null=True)  # Field name made lowercase.
    xid = models.IntegerField(db_column='XID',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '`payer_transitions`'


class Payers(models.Model):
    id = models.TextField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='ADDRESS', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='CITY', blank=True, null=True)  # Field name made lowercase.
    state_headquartered = models.TextField(db_column='STATE_HEADQUARTERED', blank=True, null=True)  # Field name made lowercase.
    zip = models.FloatField(db_column='ZIP', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='PHONE', blank=True, null=True)  # Field name made lowercase.
    amount_covered = models.FloatField(db_column='AMOUNT_COVERED', blank=True, null=True)  # Field name made lowercase.
    amount_uncovered = models.FloatField(db_column='AMOUNT_UNCOVERED', blank=True, null=True)  # Field name made lowercase.
    revenue = models.FloatField(db_column='REVENUE', blank=True, null=True)  # Field name made lowercase.
    covered_encounters = models.FloatField(db_column='COVERED_ENCOUNTERS', blank=True, null=True)  # Field name made lowercase.
    uncovered_encounters = models.FloatField(db_column='UNCOVERED_ENCOUNTERS', blank=True, null=True)  # Field name made lowercase.
    covered_medications = models.FloatField(db_column='COVERED_MEDICATIONS', blank=True, null=True)  # Field name made lowercase.
    uncovered_medications = models.FloatField(db_column='UNCOVERED_MEDICATIONS', blank=True, null=True)  # Field name made lowercase.
    covered_procedures = models.FloatField(db_column='COVERED_PROCEDURES', blank=True, null=True)  # Field name made lowercase.
    uncovered_procedures = models.FloatField(db_column='UNCOVERED_PROCEDURES', blank=True, null=True)  # Field name made lowercase.
    covered_immunizations = models.FloatField(db_column='COVERED_IMMUNIZATIONS', blank=True, null=True)  # Field name made lowercase.
    uncovered_immunizations = models.FloatField(db_column='UNCOVERED_IMMUNIZATIONS', blank=True, null=True)  # Field name made lowercase.
    unique_customers = models.FloatField(db_column='UNIQUE_CUSTOMERS', blank=True, null=True)  # Field name made lowercase.
    qols_avg = models.FloatField(db_column='QOLS_AVG', blank=True, null=True)  # Field name made lowercase.
    member_months = models.FloatField(db_column='MEMBER_MONTHS', blank=True, null=True)  # Field name made lowercase.
    xid = models.IntegerField(db_column='XID',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '`payers`'


class Procedures(models.Model):
    date = models.TextField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    patient = models.TextField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    encounter = models.TextField(db_column='ENCOUNTER', blank=True, null=True)  # Field name made lowercase.
    code = models.FloatField(db_column='CODE', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    base_cost = models.FloatField(db_column='BASE_COST', blank=True, null=True)  # Field name made lowercase.
    reasoncode = models.TextField(db_column='REASONCODE', blank=True, null=True)  # Field name made lowercase.
    reasondescription = models.TextField(db_column='REASONDESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    xid = models.IntegerField(db_column='XID',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '`procedures`'


class Providers(models.Model):
    id = models.TextField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    organization = models.TextField(db_column='ORGANIZATION', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(db_column='GENDER', blank=True, null=True)  # Field name made lowercase.
    speciality = models.TextField(db_column='SPECIALITY', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='ADDRESS', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='CITY', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    zip = models.TextField(db_column='ZIP', blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='LAT', blank=True, null=True)  # Field name made lowercase.
    lon = models.FloatField(db_column='LON', blank=True, null=True)  # Field name made lowercase.
    utilization = models.FloatField(db_column='UTILIZATION', blank=True, null=True)  # Field name made lowercase.
    xid = models.IntegerField(db_column='XID',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '`providers`'


class Supplies(models.Model):
    date = models.TextField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    patient = models.TextField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    encounter = models.TextField(db_column='ENCOUNTER', blank=True, null=True)  # Field name made lowercase.
    code = models.TextField(db_column='CODE', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    quantity = models.TextField(db_column='QUANTITY', blank=True, null=True)  # Field name made lowercase.
    xid = models.IntegerField(db_column='XID',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '`supplies`'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DoctorDoctor(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(unique=True, max_length=50)
    gender = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    age = models.IntegerField()
    department = models.CharField(max_length=30)
    specializations = models.CharField(db_column='Specializations', max_length=30)  # Field name made lowercase.
    username = models.OneToOneField(AuthUser, models.DO_NOTHING)
    phone = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'doctor_doctor'


class PatientPatient(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(unique=True, max_length=50)
    gender = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    age = models.IntegerField()
    blood = models.CharField(max_length=10)
    username = models.OneToOneField(AuthUser, models.DO_NOTHING)
    phone = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'patient_patient'

class Medication(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    substitute0 = models.TextField(blank=True, null=True)
    substitute1 = models.TextField(blank=True, null=True)
    substitute2 = models.TextField(blank=True, null=True)
    substitute3 = models.TextField(blank=True, null=True)
    substitute4 = models.TextField(blank=True, null=True)
    sideeffect0 = models.TextField(db_column='sideEffect0', blank=True, null=True)  # Field name made lowercase.
    sideeffect1 = models.TextField(db_column='sideEffect1', blank=True, null=True)  # Field name made lowercase.
    sideeffect2 = models.TextField(db_column='sideEffect2', blank=True, null=True)  # Field name made lowercase.
    sideeffect3 = models.TextField(db_column='sideEffect3', blank=True, null=True)  # Field name made lowercase.
    sideeffect4 = models.TextField(db_column='sideEffect4', blank=True, null=True)  # Field name made lowercase.
    sideeffect5 = models.TextField(db_column='sideEffect5', blank=True, null=True)  # Field name made lowercase.
    sideeffect6 = models.TextField(db_column='sideEffect6', blank=True, null=True)  # Field name made lowercase.
    sideeffect7 = models.TextField(db_column='sideEffect7', blank=True, null=True)  # Field name made lowercase.
    sideeffect8 = models.TextField(db_column='sideEffect8', blank=True, null=True)  # Field name made lowercase.
    sideeffect9 = models.TextField(db_column='sideEffect9', blank=True, null=True)  # Field name made lowercase.
    sideeffect10 = models.TextField(db_column='sideEffect10', blank=True, null=True)  # Field name made lowercase.
    sideeffect11 = models.TextField(db_column='sideEffect11', blank=True, null=True)  # Field name made lowercase.
    sideeffect12 = models.TextField(db_column='sideEffect12', blank=True, null=True)  # Field name made lowercase.
    sideeffect13 = models.TextField(db_column='sideEffect13', blank=True, null=True)  # Field name made lowercase.
    sideeffect14 = models.TextField(db_column='sideEffect14', blank=True, null=True)  # Field name made lowercase.
    sideeffect15 = models.TextField(db_column='sideEffect15', blank=True, null=True)  # Field name made lowercase.
    sideeffect16 = models.TextField(db_column='sideEffect16', blank=True, null=True)  # Field name made lowercase.
    sideeffect17 = models.TextField(db_column='sideEffect17', blank=True, null=True)  # Field name made lowercase.
    sideeffect18 = models.TextField(db_column='sideEffect18', blank=True, null=True)  # Field name made lowercase.
    sideeffect19 = models.TextField(db_column='sideEffect19', blank=True, null=True)  # Field name made lowercase.
    sideeffect20 = models.TextField(db_column='sideEffect20', blank=True, null=True)  # Field name made lowercase.
    sideeffect21 = models.TextField(db_column='sideEffect21', blank=True, null=True)  # Field name made lowercase.
    sideeffect22 = models.TextField(db_column='sideEffect22', blank=True, null=True)  # Field name made lowercase.
    sideeffect23 = models.TextField(db_column='sideEffect23', blank=True, null=True)  # Field name made lowercase.
    sideeffect24 = models.TextField(db_column='sideEffect24', blank=True, null=True)  # Field name made lowercase.
    sideeffect25 = models.TextField(db_column='sideEffect25', blank=True, null=True)  # Field name made lowercase.
    sideeffect26 = models.TextField(db_column='sideEffect26', blank=True, null=True)  # Field name made lowercase.
    sideeffect27 = models.TextField(db_column='sideEffect27', blank=True, null=True)  # Field name made lowercase.
    sideeffect28 = models.TextField(db_column='sideEffect28', blank=True, null=True)  # Field name made lowercase.
    sideeffect29 = models.TextField(db_column='sideEffect29', blank=True, null=True)  # Field name made lowercase.
    sideeffect30 = models.TextField(db_column='sideEffect30', blank=True, null=True)  # Field name made lowercase.
    sideeffect31 = models.TextField(db_column='sideEffect31', blank=True, null=True)  # Field name made lowercase.
    sideeffect32 = models.TextField(db_column='sideEffect32', blank=True, null=True)  # Field name made lowercase.
    sideeffect33 = models.TextField(db_column='sideEffect33', blank=True, null=True)  # Field name made lowercase.
    sideeffect34 = models.TextField(db_column='sideEffect34', blank=True, null=True)  # Field name made lowercase.
    sideeffect35 = models.TextField(db_column='sideEffect35', blank=True, null=True)  # Field name made lowercase.
    sideeffect36 = models.TextField(db_column='sideEffect36', blank=True, null=True)  # Field name made lowercase.
    sideeffect37 = models.TextField(db_column='sideEffect37', blank=True, null=True)  # Field name made lowercase.
    sideeffect38 = models.TextField(db_column='sideEffect38', blank=True, null=True)  # Field name made lowercase.
    sideeffect39 = models.TextField(db_column='sideEffect39', blank=True, null=True)  # Field name made lowercase.
    sideeffect40 = models.TextField(db_column='sideEffect40', blank=True, null=True)  # Field name made lowercase.
    sideeffect41 = models.TextField(db_column='sideEffect41', blank=True, null=True)  # Field name made lowercase.
    use0 = models.TextField(blank=True, null=True)
    use1 = models.TextField(blank=True, null=True)
    use2 = models.TextField(blank=True, null=True)
    use3 = models.TextField(blank=True, null=True)
    use4 = models.TextField(blank=True, null=True)
    chemical_class = models.TextField(db_column='Chemical Class', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    habit_forming = models.TextField(db_column='Habit Forming', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    therapeutic_class = models.TextField(db_column='Therapeutic Class', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    action_class = models.TextField(db_column='Action Class', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'medication_medication'