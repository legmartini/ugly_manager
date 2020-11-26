# Generated by Django 3.1.2 on 2020-11-25 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos_feios', '0018_auto_20201125_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='produto',
            name='modelo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos_feios.modelo'),
        ),
    ]
