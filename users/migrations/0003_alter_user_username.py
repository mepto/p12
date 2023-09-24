# Generated by Django 4.2.2 on 2023-08-20 21:19

from django.db import migrations
import epic.classes


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=epic.classes.LowercaseEmailField(max_length=150, unique=True),
        ),
    ]
