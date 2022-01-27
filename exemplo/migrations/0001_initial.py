# Generated by Django 2.2.7 on 2022-01-27 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vunerability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=255, verbose_name='Hostname')),
                ('ip_address', models.TextField(blank=True, null=True, verbose_name='Ip Address')),
                ('vulnerability_severity', models.CharField(blank=True, max_length=255, null=True, verbose_name='Severity')),
                ('vulnerability_cvss', models.FloatField(blank=True, null=True, verbose_name='CVSS')),
                ('vulnerability_publication_date', models.DateField(verbose_name='Publication Date')),
            ],
        ),
    ]
