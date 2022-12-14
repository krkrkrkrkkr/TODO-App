# Generated by Django 4.0.4 on 2022-07-11 13:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_datetime', models.DateTimeField()),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
