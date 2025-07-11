# python manage.py inspectdb

# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#     name = models.CharField(max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()
#     first_name = models.CharField(max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class DjangoAdminLog(models.Model):
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     action_time = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


# class FaunatrackFaunatrackuser(models.Model):
#     user = models.OneToOneField(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'faunatrack_faunatrackuser'


# class FaunatrackLocation(models.Model):
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     name = models.CharField(max_length=255)
#     longitude = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
#     lattitude = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
#     uuid = models.CharField(max_length=32)

#     class Meta:
#         managed = False 
        


# class FaunatrackObservation(models.Model):
#     uuid = models.CharField(max_length=32)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     notes = models.TextField(blank=True, null=True)
#     quantity = models.PositiveIntegerField()
#     location = models.ForeignKey(FaunatrackLocation, models.DO_NOTHING)
#     species = models.ForeignKey('FaunatrackSpecies', models.DO_NOTHING)
#     project = models.ForeignKey('FaunatrackProject', models.DO_NOTHING)
#     date_observation = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'faunatrack_observation'


# class FaunatrackObservationimage(models.Model):
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     image = models.CharField(max_length=100, blank=True, null=True)
#     observation = models.ForeignKey(FaunatrackObservation, models.DO_NOTHING, blank=True, null=True)
#     uuid = models.CharField(max_length=32)

#     class Meta:
#         managed = False
#         db_table = 'faunatrack_observationimage'


# class FaunatrackProject(models.Model):
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     is_public = models.BooleanField()
#     uuid = models.CharField(max_length=32)

#     class Meta:
#         managed = False
#         db_table = 'faunatrack_project'


# class FaunatrackProjectuseraccess(models.Model):
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     roles = models.CharField(max_length=255)
#     project = models.ForeignKey(FaunatrackProject, models.DO_NOTHING)
#     user = models.ForeignKey(FaunatrackFaunatrackuser, models.DO_NOTHING)
#     uuid = models.CharField(max_length=32)

#     class Meta:
#         managed = False
#         db_table = 'faunatrack_projectuseraccess'


# class FaunatrackSpecies(models.Model):
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     name = models.CharField(unique=True, max_length=255)
#     at_risk = models.BooleanField()
#     uuid = models.CharField(max_length=32)

#     class Meta:
#         managed = False
#         db_table = 'faunatrack_species'
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MjIyNjU1OCwiaWF0IjoxNzUyMTQwMTU4LCJqdGkiOiIxNGRjYWM1ZGQ3YmI0YmI3OTFiOGNiZTVlOWNkZmNkMSIsInVzZXJfaWQiOjF9.YMMfkTt4Yh_f4Jq85KJvW1_yZPUekDoDXX-MIp2wt1o",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyMTQwNDU4LCJpYXQiOjE3NTIxNDAxNTgsImp0aSI6IjhmZjAwNDUyODE1NjQ2OGM5ZmI0ODBkNjE3MTQ2ZGQzIiwidXNlcl9pZCI6MX0.ZnTzfh3urstd5cNAP5tqnrEkY0WZjlHfUs5c6X6O86I"
}