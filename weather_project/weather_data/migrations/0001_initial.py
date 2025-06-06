# Generated by Django 5.2 on 2025-04-15 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=50, null=True)),
                ('parameter', models.CharField(max_length=50, null=True)),
                ('year', models.IntegerField()),
                ('jan', models.FloatField(null=True)),
                ('feb', models.FloatField(null=True)),
                ('mar', models.FloatField(null=True)),
                ('apr', models.FloatField(null=True)),
                ('may', models.FloatField(null=True)),
                ('jun', models.FloatField(null=True)),
                ('jul', models.FloatField(null=True)),
                ('aug', models.FloatField(null=True)),
                ('sep', models.FloatField(null=True)),
                ('oct', models.FloatField(null=True)),
                ('nov', models.FloatField(null=True)),
                ('dec', models.FloatField(null=True)),
                ('annual', models.FloatField(null=True)),
            ],
        ),
    ]
