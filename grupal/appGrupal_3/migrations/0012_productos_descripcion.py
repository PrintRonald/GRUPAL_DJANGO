# Generated by Django 3.2.9 on 2021-12-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appGrupal_3', '0011_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='descripcion',
            field=models.TextField(default='null', max_length=500),
            preserve_default=False,
        ),
    ]
