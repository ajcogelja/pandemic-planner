# Generated by Django 3.1.2 on 2020-10-22 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandemic_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('email', models.TextField()),
                ('password', models.TextField()),
                ('credit_hours', models.IntegerField()),
            ],
        ),
    ]
