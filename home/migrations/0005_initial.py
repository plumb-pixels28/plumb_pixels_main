# Generated by Django 4.2.4 on 2024-03-26 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0004_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('reason', models.EmailField(choices=[('For my client', 'For my client'), ('other', 'other'), ('For my team', 'For my team')], max_length=100)),
                ('mssg', models.TextField()),
            ],
        ),
    ]
