# Generated by Django 3.2 on 2022-05-06 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Имя автора', max_length=100, verbose_name='Имя автора')),
                ('last_name', models.CharField(help_text='Фамилия автора', max_length=100, verbose_name='Фамилия автора')),
                ('date_of_birth', models.DateField(blank=True, help_text='Дата рождения', null=True, verbose_name='Дата рождения')),
                ('date_of_death', models.DateField(blank=True, help_text='Дата смерти', null=True, verbose_name='Дата смерти')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название книги', max_length=200, verbose_name='Название книги')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('summary', models.TextField(help_text='Введите краткое описание', max_length=1000, verbose_name='Аннотация книги')),
                ('isbn', models.CharField(help_text='Должно содержать 13 символов', max_length=13, verbose_name='ISBN книги')),
                ('author', models.ManyToManyField(help_text='Выборите автор книги', null=True, to='catalog.Author', verbose_name='автор книги')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите жанр книги', max_length=200, verbose_name='Жанр книги')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите язык книги', max_length=20, verbose_name='Язык книги')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Должно содержать 13 символов', max_length=20, verbose_name='ISBN книги')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_nom', models.CharField(help_text='Введите инвентарный номер экземпляра', max_length=20, null=True, verbose_name='Инвентарный номер')),
                ('imprint', models.CharField(help_text='Введите издательство и год выnуска', max_length=200, verbose_name='Издательство')),
                ('due_back', models.DateField(blank=True, help_text='Введите конец срока статуса', null=True, verbose_name='Дaтa окончания статуса')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.book')),
                ('status', models.ForeignKey(help_text='Изменить состояние экземпляра', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.status', verbose_name='Cтaтyc экземпляра книги')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text='Выберите жанр книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.genre', verbose_name='Жанр книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='Выберите язык книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.language', verbose_name='язык книги'),
        ),
    ]
