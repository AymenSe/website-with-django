# Generated by Django 2.1.7 on 2019-04-26 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190426_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField()),
                ('headline', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='add_images/')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.NewReporter')),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='reporter',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
