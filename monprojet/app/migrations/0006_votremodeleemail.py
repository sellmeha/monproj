# Generated by Django 4.2 on 2024-03-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_teacher_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotreModeleEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse_email', models.EmailField(max_length=255)),
            ],
        ),
    ]
