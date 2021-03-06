# Generated by Django 3.2.9 on 2021-12-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('age', models.IntegerField(default=False)),
                ('department', models.CharField(max_length=120)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('entry_timestamp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
