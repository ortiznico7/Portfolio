# Generated by Django 5.1.6 on 2025-04-02 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfinance', '0002_language_framework'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Framework',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
