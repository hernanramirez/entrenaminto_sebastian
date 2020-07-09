# Generated by Django 3.0.8 on 2020-07-09 21:44

from django.db import migrations, models
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', model_utils.fields.StatusField(choices=[('Familia', 'Familia'), ('Trabajo', 'Trabajo')], default='Familia', max_length=100, no_check_for_status=True)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
    ]
