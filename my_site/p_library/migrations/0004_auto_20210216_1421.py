# Generated by Django 3.0.2 on 2021-02-16 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20210204_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(verbose_name='Имя')),
                ('phone', models.CharField(blank=True, max_length=16, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Друг',
                'verbose_name_plural': 'Друзья',
            },
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='publishinghouse',
            options={'verbose_name': 'Издательство', 'verbose_name_plural': 'Издательства'},
        ),
        migrations.CreateModel(
            name='WhenTook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when_took', models.DateField(verbose_name='Какого числа была взята книга')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Book', verbose_name='Книга')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Friend', verbose_name='Друг')),
            ],
            options={
                'verbose_name': 'Книга у друга',
                'verbose_name_plural': 'Книги у друзей',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='friends',
            field=models.ManyToManyField(through='p_library.WhenTook', to='p_library.Friend'),
        ),
    ]
