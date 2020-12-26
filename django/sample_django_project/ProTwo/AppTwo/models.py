from django.db import models

# Create your models here.
class Book(models.Model):
    book_language = models.CharField(max_length=50,unique=False)
    book_Name = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return str(self.book_Name)

class BookInfo(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    name = models.CharField(max_length=30,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name




