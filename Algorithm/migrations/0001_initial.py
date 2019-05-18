# Generated by Django 2.2.1 on 2019-05-18 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=20000)),
                ('algo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Algorithm.Algorithm')),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Algorithm.Language')),
            ],
        ),
        migrations.AddField(
            model_name='algorithm',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Algorithm.Category'),
        ),
        migrations.AddField(
            model_name='algorithm',
            name='langs',
            field=models.ManyToManyField(to='Algorithm.Language'),
        ),
    ]
