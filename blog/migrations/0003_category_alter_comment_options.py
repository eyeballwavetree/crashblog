# Generated by Django 4.1.2 on 2022-10-17 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_options_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created_at',)},
        ),
    ]