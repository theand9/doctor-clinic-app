<<<<<<< HEAD
# Generated by Django 3.0.3 on 2020-04-02 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('is_Doctor', models.BooleanField(default=False)),
                ('is_Patient', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(choices=[('MBBS', 'MBBS'), ('BDS', 'BDS'), ('BHMS', 'BHMS'), ('DHMS', 'DHMS'), ('BAMS', 'BAMS'), ('BUMS', 'BUMS'), ('BVSc & AH', 'BVSc & AH'), ('B.Pharm.', 'B.Pharm.'), ('D.Pharm.', 'D.Pharm.'), ('BOT', 'BOT'), ('BMLT', 'BMLT'), ('BPT', 'BPT'), ('B.Sc. Nursing', 'B.Sc. Nursing'), ('BNYS', 'BNYS')], default='MBBS', max_length=50)),
                ('postgrad', models.CharField(choices=[('None', 'None'), ('MD', 'MD'), ('MS', 'MS'), ('Diploma', 'Diploma')], default=None, max_length=50, null=True)),
                ('speciality', models.CharField(choices=[('None', 'None'), ('DM', 'DM'), ('MCh', 'MCh')], default=None, max_length=50, null=True)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOB', models.DateField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic_app.Doctor')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('published_on', models.DateTimeField()),
                ('file', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic_app.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('token_number', models.IntegerField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic_app.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic_app.Patient')),
            ],
        ),
    ]
=======
# Generated by Django 2.2.11 on 2020-03-21 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('is_Doctor', models.BooleanField(default=False)),
                ('is_Patient', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(choices=[('MBBS', 'MBBS'), ('BDS', 'BDS'), ('BHMS', 'BHMS'), ('DHMS', 'DHMS'), ('BAMS', 'BAMS'), ('BUMS', 'BUMS'), ('BVSc & AH', 'BVSc & AH'), ('B.Pharm.', 'B.Pharm.'), ('D.Pharm.', 'D.Pharm.'), ('BOT', 'BOT'), ('BMLT', 'BMLT'), ('BPT', 'BPT'), ('B.Sc. Nursing', 'B.Sc. Nursing'), ('BNYS', 'BNYS')], default='MBBS', max_length=50)),
                ('postgrad', models.CharField(choices=[('None', 'None'), ('MD', 'MD'), ('MS', 'MS'), ('Diploma', 'Diploma')], default=None, max_length=50, null=True)),
                ('speciality', models.CharField(choices=[('None', 'None'), ('DM', 'DM'), ('MCh', 'MCh')], default=None, max_length=50, null=True)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOB', models.DateField(default=django.utils.timezone.now, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic_app.Doctor')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('published_on', models.DateTimeField()),
                ('file', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic_app.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('token_number', models.IntegerField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic_app.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic_app.Patient')),
            ],
        ),
    ]
>>>>>>> Appointments fetch working
