# Generated by Django 3.0.1 on 2020-01-30 11:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogadd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('blog', models.CharField(max_length=1000)),
                ('date', models.DateField(default=datetime.datetime(2020, 1, 30, 17, 25, 12, 99291))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Adduser')),
            ],
        ),
    ]