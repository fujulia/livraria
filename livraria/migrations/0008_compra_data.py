# Generated by Django 5.0.4 on 2024-04-07 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0007_itenscompra_preco_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
