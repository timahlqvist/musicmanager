from django.db import models

# Create your models here.

class Record(models.Model):
    artist = models.CharField(max_length=200)
    record_name = models.CharField(max_length=400)
    genre = models.CharField(max_length=200)
    contributor = models.CharField(max_length=400)
    label = models.CharField(max_length=400)
    logo = models.CharField(max_length=1000)
    record_format = models.CharField(max_length=200)
    year = models.IntegerField()
    record_number = models.CharField(max_length=400)

    def __str__(self):
        return self.artist + ' - ' + self.record_name