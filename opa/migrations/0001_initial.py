# Generated by Django 3.0.3 on 2020-03-16 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OPAStatusBundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('last_successful_activation', models.CharField(max_length=256)),
                ('last_successful_download', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=256)),
                ('message', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='OPAStatusLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=256)),
                ('environment', models.CharField(max_length=256)),
                ('uuid', models.CharField(max_length=256)),
                ('region', models.CharField(max_length=256)),
                ('version', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='OPAStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bundle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opa.OPAStatusBundle')),
                ('labels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opa.OPAStatusLabel')),
            ],
        ),
    ]
