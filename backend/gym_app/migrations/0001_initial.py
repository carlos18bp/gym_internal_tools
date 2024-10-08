# Generated by Django 5.0.6 on 2024-09-25 23:36

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=60, null=True)),
                ('last_name', models.CharField(blank=True, max_length=60, null=True)),
                ('contact', models.CharField(blank=True, help_text='The contact number of the user.', max_length=15, null=True)),
                ('birthday', models.DateField(blank=True, help_text='The birth date of the user.', null=True)),
                ('identification', models.CharField(blank=True, help_text='The identification number of the user.', max_length=20, null=True)),
                ('marital_status', models.CharField(blank=True, help_text='The marital status of the user (e.g., single, married).', max_length=20, null=True)),
                ('role', models.CharField(blank=True, default='client', help_text="The role of the user within the system (default: 'client').", max_length=50, null=True)),
                ('photo_profile', models.ImageField(blank=True, help_text='The profile picture of the user.', null=True, upload_to='profile_photos/')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date the user was created.')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='The type of the case.', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CaseFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(help_text='The file associated with the case.', upload_to='case_files/')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date the file was uploaded.')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(help_text='The current status of the stage.', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date the stage was created.')),
            ],
        ),
        migrations.CreateModel(
            name='PasswordCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(code='invalid_code', message='Code must be 6 digits', regex='^\\d{6}$')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('used', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Password Code',
                'verbose_name_plural': 'Password Codes',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authority', models.CharField(help_text='The authority handling the case.', max_length=100)),
                ('plaintiff', models.CharField(help_text='The person initiating the legal action.', max_length=100)),
                ('defendant', models.CharField(help_text='The person against whom the action is brought.', max_length=100)),
                ('ref', models.CharField(help_text='The unique file number or case ID.', max_length=100, unique=True)),
                ('subcase', models.CharField(help_text='The subcase classification.', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date the process was created.')),
                ('case', models.ForeignKey(help_text='The case type being processed.', on_delete=django.db.models.deletion.CASCADE, to='gym_app.case')),
                ('case_files', models.ManyToManyField(help_text='The case files associated with the process.', to='gym_app.casefile')),
                ('client', models.ForeignKey(help_text='The client associated with the process.', on_delete=django.db.models.deletion.CASCADE, related_name='client_processes', to=settings.AUTH_USER_MODEL)),
                ('lawyer', models.ForeignKey(help_text='The lawyer handling the case.', on_delete=django.db.models.deletion.CASCADE, related_name='lawyer_processes', to=settings.AUTH_USER_MODEL)),
                ('stages', models.ManyToManyField(help_text='The stages associated with the process.', to='gym_app.stage')),
            ],
        ),
    ]
