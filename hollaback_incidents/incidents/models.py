from django.db import models

class LocationType(models.Model):
    """Represents a type of location e.g. on the metro."""
    visible = models.BooleanField(default=True)
    label = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.label

class Incident(models.Model):
    """Represents a harassment incident."""
    visible = models.BooleanField(default=False)
    place = models.CharField(max_length=255)
    location_type = models.ManyToManyField(LocationType)
    other_type = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    story = models.TextField()
    signature = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    def __unicode__(self):
        return self.title