# Generated by Django 3.2.3 on 2021-07-23 07:54

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Phone', models.CharField(max_length=13)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], default='male', max_length=15)),
                ('user_type', models.CharField(choices=[('employer', 'employer'), ('jobseeker', 'jobseeker')], default='employer', max_length=12)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='EmployerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_address', models.CharField(max_length=120)),
                ('company_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JsJobModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_role', models.CharField(max_length=20)),
                ('company_name', models.CharField(default='', max_length=30)),
                ('job_details', models.CharField(max_length=120)),
                ('exp_required', models.CharField(max_length=15)),
                ('openings', models.IntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Closed', 'Closed')], default='Active', max_length=10)),
                ('starting_date', models.DateField(auto_now=True)),
                ('last_date', models.DateField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.employermodel')),
            ],
        ),
        migrations.CreateModel(
            name='JobseekerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=20)),
                ('University', models.CharField(max_length=20)),
                ('skills', models.CharField(max_length=200)),
                ('experience', models.FloatField()),
                ('expected_salary', models.IntegerField()),
                ('ready_to_relocate', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_role', models.CharField(max_length=20)),
                ('company_name', models.CharField(default='', max_length=30)),
                ('job_details', models.CharField(max_length=120)),
                ('exp_required', models.CharField(max_length=15)),
                ('openings', models.IntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Closed', 'Closed')], default='Active', max_length=10)),
                ('starting_date', models.DateField(auto_now=True)),
                ('last_date', models.DateField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.employermodel')),
            ],
        ),
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_seeker', models.CharField(default='', max_length=20)),
                ('status', models.CharField(choices=[('received', 'received'), ('viewed', 'viewed'), ('selected', 'selected'), ('rejected', 'rejected')], default='Received', max_length=20)),
                ('job', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='jobapp.jobmodel')),
            ],
        ),
    ]