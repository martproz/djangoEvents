from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    adress = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=15)
    phone = models.CharField('Contact Phone', max_length=25, blank=True)
    web = models.URLField('Website Address', blank=True)
    email_adress = models.EmailField('Email Adress', blank=True)
    venue_image = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return self.name

class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Event(models.Model):
    name = models.CharField('Events Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(
        Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)


    def __str__(self):
        return self.name

    #venue_image = models.ImageField(null=True, blank=True, upload_to='images/')
    #upload to goes to media directory, settings, media root media, as
    # soon as we create an image, the media directory will be created automatically
    # inside that media file will be a subdirectory called images
    # where all our images will be saved
