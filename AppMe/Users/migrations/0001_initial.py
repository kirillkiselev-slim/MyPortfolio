# Generated by Django 4.2.3 on 2023-07-12 02:21

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
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=120)),
                ('age', models.PositiveIntegerField()),
                ('username', models.CharField(max_length=120, unique=True)),
                ('password', models.CharField(max_length=120)),
                ('email', models.EmailField(blank=True, default=True, max_length=240, null=True)),
            ],
        ),
    ]
