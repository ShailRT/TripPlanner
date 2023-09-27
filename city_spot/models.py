from django.db import models
import uuid

class Gallery(models.Model):
    title = models.CharField
    image = models.ImageField(upload_to="gallery/")

class Spot(models.Model):
    spot_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    main_image = models.ImageField(upload_to="spot_image/")
    gallery = models.ManyToManyField(Gallery, null=True, blank=True)
    description = models.TextField()
    location = models.CharField(max_length=400)

    def __str__(self):
        return self.name


