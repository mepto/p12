# Generated by Django 4.2.5 on 2023-10-02 14:21

from django.db import migrations, models
import epic.classes


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatusContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', epic.classes.CapitalizeField(blank=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='StatusEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', epic.classes.CapitalizeField(blank=True, max_length=25)),
            ],
        ),
    ]
