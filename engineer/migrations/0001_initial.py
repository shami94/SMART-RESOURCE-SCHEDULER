# Generated by Django 4.0.5 on 2023-02-27 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('customer', '0001_initial'),
        ('admin', '0003_alter_equipment_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstructionLabour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
                ('position', models.CharField(max_length=255)),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=7)),
                ('engineer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.siteengineer')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectAssignLabour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_date', models.DateTimeField(auto_now_add=True)),
                ('labour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engineer.constructionlabour')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectAssignEquipments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_date', models.DateTimeField(auto_now_add=True)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.equipment')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.project')),
            ],
        ),
    ]
