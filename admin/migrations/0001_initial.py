# Generated by Django 4.0.5 on 2023-02-26 14:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('equipment_type', models.CharField(choices=[('excavator', 'Excavator'), ('bulldozer', 'Bulldozer'), ('crane', 'Crane'), ('loader', 'Loader')], max_length=20)),
                ('rent_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.CharField(choices=[('available', 'Available'), ('scheduled', 'Scheduled'), ('in_use', 'In Use'), ('in_repair', 'In Repair')], default='available', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HouseDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('style', models.CharField(choices=[('modern', 'Modern'), ('traditional', 'Traditional'), ('contemporary', 'Contemporary'), ('rustic', 'Rustic')], max_length=20)),
                ('square_footage', models.IntegerField()),
                ('num_bedrooms', models.IntegerField()),
                ('num_bathrooms', models.IntegerField()),
                ('num_floors', models.IntegerField()),
                ('garage', models.CharField(choices=[('none', 'None'), ('attached', 'Attached'), ('detached', 'Detached')], default='none', max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='house_designs/')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_date', models.DateTimeField(auto_now_add=True)),
                ('engineer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.siteengineer')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.project')),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentRentBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField()),
                ('quantity', models.PositiveIntegerField()),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_approved', models.BooleanField(default=False)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.equipment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
