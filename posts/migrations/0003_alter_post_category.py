# Generated by Django 4.1.5 on 2023-01-25 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('book', '책'), ('charger', '충전기'), ('calculator', '계산기'), ('student product', '학생용품'), ('lost item', '분실물'), ('etx', '그 외')], default='lost item', max_length=40),
        ),
    ]