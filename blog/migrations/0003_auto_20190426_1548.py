# Generated by Django 2.1.7 on 2019-04-26 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190426_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewReporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=64)),
                ('s_name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=256)),
                ('data_birth', models.DateField()),
                ('domain', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='reporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.NewReporter'),
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
    ]
