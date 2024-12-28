from django.db import models

# Create your models here.
class Movie(models.Model):
    Title = models.CharField(max_length=30)
    YearOfRelease = models.IntegerField()
    Genre = models.CharField(max_length=30)
    IMDBRating = models.FloatField(blank=True,null=True)
    Plot = models.CharField(max_length=500)
    Cast = models.CharField(max_length=60)
    Director = models.CharField(max_length=30)
    Runtime = models.FloatField(blank=True,null=True)
    CHOICES = [
        ('hindi','Hindi'),
        ('tamil','Tamil'),
        ('malayalam','Malayalam'),
        ('english','English')
    ]
    Language = models.CharField(choices=CHOICES,max_length=45,blank=True)
    Favourite = models.BooleanField(default=False)
    
    def __str__(self):
        return self.Title
