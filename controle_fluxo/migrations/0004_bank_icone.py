# Generated by Django 4.2.2 on 2023-08-23 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_fluxo', '0003_owner_alter_bank_value_activities_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='icone',
            field=models.FileField(blank=True, null=True, upload_to='bank/'),
        ),
    ]