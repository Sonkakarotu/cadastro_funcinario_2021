# Generated by Django 3.1.5 on 2021-01-18 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='funcao',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
