# Generated by Django 4.2.4 on 2024-03-26 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_contact_name_alter_contact_reason'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
