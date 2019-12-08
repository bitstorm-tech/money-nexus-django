# Generated by Django 3.0 on 2019-12-08 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('note', models.TextField(null=True)),
                ('bill_image', models.ImageField(null=True, upload_to='')),
                ('tags', models.ManyToManyField(to='tags.Tag')),
            ],
        ),
    ]