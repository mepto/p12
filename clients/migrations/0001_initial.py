# Generated by Django 4.2.2 on 2023-08-20 21:03

from django.db import migrations, models
import django.db.models.deletion
import epic.classes


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', epic.classes.CapitalizeField(max_length=255)),
                ('first_name', epic.classes.CapitalizeField(blank=True, max_length=25)),
                ('last_name', epic.classes.UppercaseField(blank=True, max_length=25)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('mobile', models.CharField(blank=True, max_length=20)),
                ('address', models.TextField()),
                ('is_prospect', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('primary_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_clients', to='users.usersales')),
                ('users', models.ManyToManyField(related_name='clients', to='users.usersales')),
            ],
            options={
                'ordering': ['company'],
            },
        ),
    ]
