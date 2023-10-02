# Generated by Django 4.2.5 on 2023-10-02 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('epic', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, help_text='Amounts should always be entered in cents')),
                ('due_date', models.DateField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='clients.client')),
                ('status_contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='epic.statuscontract')),
            ],
            options={
                'ordering': ['-due_date'],
            },
        ),
    ]
