# Generated by Django 4.2.4 on 2024-03-26 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_contact_reson_contact_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='reason',
            field=models.CharField(choices=[('For my team', 'For my team'), ('For my client', 'For my client'), ('other', 'other')], default='null', max_length=100),
        ),
    ]
