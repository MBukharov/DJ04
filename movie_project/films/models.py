from django.db import models

# Create your models here.
class Film(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название фильма")
    description = models.TextField(verbose_name="Описание")
    comment = models.CharField(max_length=100, verbose_name="Отзыв о фильме")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"