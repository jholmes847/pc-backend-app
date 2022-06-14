# Generated by Django 4.0.5 on 2022-06-14 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='case',
            field=models.CharField(default='Case', max_length=32),
        ),
        migrations.AddField(
            model_name='post',
            name='cooler',
            field=models.CharField(default='Cooler', max_length=32),
        ),
        migrations.AddField(
            model_name='post',
            name='gpu',
            field=models.CharField(default='GPU', max_length=32),
        ),
        migrations.AddField(
            model_name='post',
            name='mobo',
            field=models.CharField(default='MOBO', max_length=32),
        ),
        migrations.AddField(
            model_name='post',
            name='post',
            field=models.CharField(default='Post', max_length=32),
        ),
        migrations.AddField(
            model_name='post',
            name='psu',
            field=models.CharField(default='PSU', max_length=32),
        ),
        migrations.AddField(
            model_name='post',
            name='ram',
            field=models.CharField(default='RAM', max_length=32),
        ),
        migrations.AddField(
            model_name='post',
            name='storage',
            field=models.CharField(default='Storage', max_length=32),
        ),
        migrations.AlterField(
            model_name='post',
            name='cpu',
            field=models.CharField(default='CPU', max_length=32),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(default='PC Name', max_length=32),
        ),
    ]