# Generated by Django 3.2.3 on 2021-06-04 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_receita_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
