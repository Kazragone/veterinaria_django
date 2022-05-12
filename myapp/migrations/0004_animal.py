# Generated by Django 4.0.3 on 2022-04-27 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_cliente_created_at_cliente_updated_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(choices=[(0, 'Mamiferos'), (1, 'Aves'), (2, 'Reptiles'), (3, 'Ranas y sapos')], default=0, max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]