from django.db import models
from django.db import models
from django.utils.text import slugify
from datetime import date

class Movie(models.Model):
    film_image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name="Постер")
    film_name = models.CharField(verbose_name="Название фильм", max_length=50)
    summary = models.TextField(verbose_name='краткое содержание', max_length=500)
    premiere = models.DateField(("премьера(гггг.мм.дд)"), auto_now=False, auto_now_add=False)
    slug = models.SlugField(max_length=255, verbose_name="Название сьраницы", unique=True, db_index=True )
    film_video = models.FileField(upload_to='video/', blank=True, null=True, verbose_name="Видео")
    AGE_RATING_CHOICES = (
        ('0+', '0+'),
        ('6+', '6+'),
        ('12+', '12+'),
        ('16+', '16+'),
        ('18+', '18+'),)
    age_rating = models.CharField(
        max_length=3,
        choices=AGE_RATING_CHOICES,
        verbose_name="Возрастной рейтинг")
    genere = models.ManyToManyField("Genere", verbose_name=('Жанр'), related_name='movies')
    actor = models.ManyToManyField("Actor", verbose_name=("Актер"), related_name='movies')
    filmmaker = models.ManyToManyField("Filmmaker", verbose_name=("Режисер"), related_name='movies')
    produser = models.ManyToManyField("Produser", verbose_name=("Продюсер"), related_name='movies')
    date=models.DateField(verbose_name='дата добавления', auto_now_add=True, auto_now=False, blank=True, null=True)
    date_ad=models.DateField(verbose_name='Дата изменения', auto_now=True, blank=True, null=True)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return f'{self.id} - {self.film_name}'
    

class Person(models.Model):
    avatar = models.ImageField(upload_to='acters_images/', blank=True, null=True, verbose_name="Аватар")
    name=models.CharField(verbose_name=("Имя Фамилия"), max_length=50)
    year_of_birth=models.DateField(verbose_name=('год рождения'))

    @property
    def age(self):  
        today = date.today()
        return (
            today.year - self.year_of_birth.year -
            ((today.month, today.day) < (self.year_of_birth.month, self.year_of_birth.day))
        )
    date=models.DateField(verbose_name='дата добавления', auto_now_add=True, auto_now=False, blank=True, null=True)
    date_ad=models.DateField(verbose_name='Дата изменения', auto_now=True, blank=True, null=True)
    def __str__(self):
        return  f'{self.id} - {self.name} ({self.age})'
    
    class Meta:
        abstract = True

class Actor(Person):
    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'


class Filmmaker(Person):
    class Meta:
        verbose_name = 'Режисер'
        verbose_name_plural = 'Режисеры'

class Produser(Person):
    class Meta:
        verbose_name = 'Продюсер'
        verbose_name_plural = 'Продюсеры'

class Genere(models.Model):
    genere_name = models.CharField(max_length=100, verbose_name="Жанр")

    def __str__(self):
        return f'{self.id} - {self.genere_name}'
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


