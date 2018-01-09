from django.db import models

class Post(models.Model): #по сути это таблица
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self): #возвращает нам title
        return self.title

