from django.utils.translation import gettext as _
from django.db import models
from django.contrib.auth.models import User
import time


class UserProfile(models.Model):
    age = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')


class Author(models.Model):
    full_name = models.TextField(verbose_name=_("Имя автора"))
    birth_year = models.SmallIntegerField(verbose_name=_("Год рожения"))
    country = models.CharField(max_length=2, verbose_name=_("Страна"))

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.full_name

class PublishingHouse(models.Model):
    name = models.TextField(verbose_name=_("Издательство"))
    country = models.CharField(null='-', max_length=2, verbose_name=_("Страна"))
    city = models.TextField(null='-', verbose_name=_("Город"))

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'

    def __str__(self):
        return self.name

class Friend(models.Model):
    full_name = models.TextField(verbose_name="Имя")
    phone = models.CharField(max_length=16, blank=True, verbose_name="Телефон")

    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'

    def __str__(self):
        return self.full_name

class Book(models.Model):
    ISBN = models.CharField(max_length=13,
                            verbose_name=_("Международный стандартный "
                                           "книжный номер"))
    title = models.TextField(verbose_name=_("Название"))
    description = models.TextField(verbose_name=_("Аннотация"))
    year_release = models.SmallIntegerField(verbose_name=_("Год издания"))
    copy_count = models.SmallIntegerField(verbose_name=_("Число копий"))
    price = models.DecimalField(max_digits=12, decimal_places=2,
                                verbose_name=_("Цена"))
    author = models.ForeignKey("p_library.Author", on_delete=models.CASCADE,
                               verbose_name=_("Автор"),
                               related_name="book_author")
    pub_house = models.ForeignKey(PublishingHouse, on_delete=models.SET_NULL, null=True, blank=True, related_name='books')
    image = models.ImageField(upload_to='images_books', blank=True, verbose_name="Изображение")
    friends = models.ManyToManyField(Friend, through='WhenTook')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title

    @property
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

class WhenTook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE, verbose_name="Друг")
    when_took = models.DateField(verbose_name="Какого числа была взята книга")

    class Meta:
        verbose_name = 'Книга у друга'
        verbose_name_plural = 'Книги у друзей'

    def __str__(self):
        return "Книгу '{}' взял '{}', {}".format(
            self.book, self.friend, time.strftime("%d.%m.%Y", time.strptime(self.when_took.ctime())))



