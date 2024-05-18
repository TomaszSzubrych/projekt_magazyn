# Generated by Django 4.1.5 on 2023-01-21 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system_mag', '0003_alter_magazyn_kategoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magazyn',
            name='export_do_CSV',
        ),
        migrations.AlterField(
            model_name='magazyn',
            name='kategoria',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='system_mag.kategoria'),
        ),
    ]