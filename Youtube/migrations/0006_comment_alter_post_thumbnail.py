# Generated by Django 5.0.6 on 2024-07-29 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0005_alter_post_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='タイトル')),
                ('text', models.TextField(verbose_name='本文')),
                ('good', models.IntegerField(verbose_name='いいね')),
                ('usertext', models.CharField(default='a', max_length=30)),
                ('username', models.CharField(default='a', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='日付')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='media/thumbnail/', verbose_name='画像'),
        ),
    ]
