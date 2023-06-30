# Generated by Django 4.2.2 on 2023-06-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modified')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('input', models.BooleanField(default=True, verbose_name='Entrada?')),
                ('description', models.TextField(max_length=200, verbose_name='Descrição')),
                ('bank', models.CharField(choices=[('Picpay', 'Picpay'), ('Nubank', 'Nubank'), ('Banco do Brasil', 'Banco do Brasil'), ('Espécie', 'Espécie')], max_length=15)),
                ('proof', models.FileField(blank=True, null=True, upload_to='comprovantes/')),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
    ]
