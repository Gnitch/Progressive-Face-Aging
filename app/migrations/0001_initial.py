# Generated by Django 3.2.3 on 2021-12-11 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father', models.CharField(max_length=150)),
                ('mother', models.CharField(max_length=150)),
                ('brother', models.CharField(blank=True, max_length=150)),
                ('sister', models.CharField(blank=True, max_length=150)),
                ('guardian', models.CharField(blank=True, max_length=150)),
                ('contact1', models.IntegerField()),
                ('contact2', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Missing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('t', 'Transgender'), ('none', 'Prefer Not To Say')], default='none', max_length=25)),
                ('state', models.CharField(choices=[('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CT', 'Chhattisgarh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OD', 'Odisha'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TG', 'Telangana'), ('TR', 'Tripura'), ('UT', 'Uttarakhand'), ('UP', 'Uttar Pradesh'), ('WB', 'West Bengal'), ('AN', 'Andaman and Nicobar Islands'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli'), ('PY', 'Puducherry'), ('LD', 'Lakshadweep'), ('DL', 'Delhi'), ('DD', 'Daman and Diu')], default='DL', max_length=30)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('weight', models.FloatField(blank=True)),
                ('height', models.FloatField(blank=True)),
                ('city', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('adhar', models.IntegerField(blank=True)),
                ('last_sighted', models.DateField()),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.family')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
