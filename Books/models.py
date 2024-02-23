from django.db import models

# Create your models here.
class LibraryBook(models.Model):
    title = models.CharField(max_length=63)
    author = models.CharField(max_length=63)
    isbn = models.CharField(max_length=63, unique=True)
    available = models.BooleanField()

    class Meta:
        verbose_name = "Library Book"
        verbose_name_plural = "Library Books"
        db_table = "library_books"
        ordering = ["author"]
