# Generated by Django 5.0.6 on 2024-09-01 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_schemedata_options_alter_userdata_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schemedata',
            options={'ordering': ['scheme_name']},
        ),
        migrations.AlterModelOptions(
            name='userdata',
            options={'ordering': ['user_name']},
        ),
    ]
