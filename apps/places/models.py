from django.db import models
from cloudinary.models import CloudinaryField
from apps.categories.models import Category

# Create your models here.

class Place(models.Model):
    MY_CHOICES = (
        ('National Landmark', 'National Landmark'),
        ('Building', 'Building'),
        ('Architectural Structure', 'Architectural Structure'),
        ('Open Attraction', 'Open Attraction'),
        ('Favourites', 'Favourites'),
    )
    class Meta(object):
        db_table = 'place'

    name = models.CharField(
        'Name', max_length=50, db_index=True, null=False, blank=False
    )

    description = models.CharField(
        'Description', max_length=500, db_index=True, null=False, blank=False
    )

    image = CloudinaryField(
        'Image', blank=False
    )
    category = models.ForeignKey(
        Category , on_delete=models.CASCADE
    )

    place_type = models.CharField(
        'Place Type', max_length=50, null=False, blank=False, choices= MY_CHOICES
    )

    time_to_travel = models.CharField(
        'Time To Travel', max_length=50, null=False, blank=False
    )
    google_map_link = models.CharField(
        'Google Map Link', max_length=500, null=False, blank=False
    )

    created_at = models.DateField(
        'Created_at' , auto_now_add=True, null=False, blank=False
    )

    updated_at = models.DateField(
        'Updated_at', auto_now_add=True, null=False, blank=False
    )

    def __str__(self):
        return self.name
