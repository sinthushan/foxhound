# Generated by Django 5.1 on 2024-08-17 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('applied_date', models.DateField(auto_now_add=True)),
                ('modefied_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(choices=[('AP', 'Applied'), ('IN', 'Interview'), ('RE', 'Rejected'), ('OF', 'Offer')], default='AP', max_length=2)),
                ('round', models.IntegerField(blank=True)),
                ('comment', models.TextField(max_length=500)),
            ],
        ),
    ]
