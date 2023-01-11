from datetime import date

from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    Category Model
    """
    name = models.CharField('Category', max_length=150)
    description = models.TextField('Description')
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Actor(models.Model):
    """
    Actors and Producer Model
    """
    name = models.CharField('Name', max_length=100)
    age = models.PositiveSmallIntegerField('Age', default=0)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actors and Producers'
        verbose_name_plural = 'Actors and Producers'


class Genre(models.Model):
    """
    Genre Model
    """
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description')
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Movie(models.Model):
    """
    Movie Model
    """
    title = models.CharField('Title', max_length=100)
    tagline = models.CharField('Tagline', max_length=100, default='')
    description = models.TextField('Description')
    poster = models.ImageField('Poster', upload_to='movies/')
    year = models.PositiveSmallIntegerField('Release date', default=2023)
    country = models.CharField('Country', max_length=30)
    producers = models.ManyToManyField(Actor, verbose_name='Producers', related_name='film_producer')
    actors = models.ManyToManyField(Actor, verbose_name='Actors', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='Genres')
    world_premiere = models.DateField('World premiere', default=date.today)
    budget = models.PositiveIntegerField('Budget', default=0, help_text='Provide amount in USD')
    fees_in_usa = models.PositiveIntegerField('Fees in USA', default=0, help_text='Provide amount in USD')
    fees_in_world = models.PositiveIntegerField('Fees in World', default=0, help_text='Provide amount in USD')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField('Draft', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class MovieShots(models.Model):
    """
    Movie Shots Model
    """
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Film', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Shot from movie'
        verbose_name_plural = 'Shots from movie'


class RatingStar(models.Model):
    """
    Rating Star Model
    """
    value = models.SmallIntegerField('Value', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Rating star'
        verbose_name_plural = 'Rating stars'


class Rating(models.Model):
    """
    Rating Model
    """
    ip = models.CharField('IP', max_length=15)
    star = models.ForeignKey(RatingStar, verbose_name='Stars', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, verbose_name='Film', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.start} - {self.movie}'

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Rating'


class Reviews(models.Model):
    """
    Reviews Model
    """
    email = models.EmailField()
    name = models.CharField('Name', max_length=100)
    text = models.TextField('Message', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Parent', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='Film', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
