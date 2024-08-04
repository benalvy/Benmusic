from django.db import models
    
 
class info(models.Model):
    Sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    
class source(models.Model):
    Sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    audio_file = models.FileField(upload_to='songs')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artists = models.ManyToManyField(Artist)
  