# Generated by Django 3.1.2 on 2020-11-26 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos_feios', '0024_auto_20201126_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModoEntrega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modo_de_entrega', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='produto',
            name='modo_de_entrega',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos_feios.modoentrega'),
        ),
    ]
