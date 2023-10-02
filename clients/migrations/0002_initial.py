# Generated by Django 4.2.5 on 2023-10-02 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='primary_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_clients', to='users.usersales'),
        ),
        migrations.AddField(
            model_name='client',
            name='users',
            field=models.ManyToManyField(related_name='clients', to='users.usersales'),
        ),
    ]