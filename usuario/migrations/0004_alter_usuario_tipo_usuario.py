# Generated by Django 5.0.4 on 2024-04-13 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_usuario_tipo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.IntegerField(choices=[(1, 'Cliente'), (2, 'Vendedor'), (3, 'Gerente')], default=1, verbose_name='User Type'),
        ),
    ]