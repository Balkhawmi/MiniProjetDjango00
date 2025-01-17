# Generated by Django 5.1.2 on 2024-10-10 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('poste', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_embauche', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Dirigeant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('droits_supplémentaires', models.BooleanField(default=True)),
                ('employe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employes.employe')),
            ],
        ),
        migrations.CreateModel(
            name='Conge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_conge', models.CharField(choices=[('CP', 'Congé Payé'), ('RTT', 'Réduction du Temps de Travail'), ('MAL', 'Maladie')], max_length=3)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('statut', models.CharField(default='En attente', max_length=10)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employes.employe')),
            ],
        ),
    ]
