# Generated by Django 4.1.2 on 2022-10-28 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newstats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win', models.IntegerField()),
                ('mac', models.IntegerField()),
                ('iph', models.IntegerField()),
                ('android', models.IntegerField()),
                ('oth', models.IntegerField()),
            ],
        ),
    ]
