# Generated by Django 5.0.6 on 2024-09-01 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_schemedata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schemedata',
            old_name='scheme_benifits',
            new_name='scheme_benefits',
        ),
    ]
