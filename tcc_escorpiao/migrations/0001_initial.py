# Generated by Django 2.2.20 on 2021-06-01 16:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escorpiao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presenca', models.CharField(max_length=200)),
                ('data_encontro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]