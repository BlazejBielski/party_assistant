from django.db import models
from django.utils.text import slugify

from dishes.validators import validate_file_type
from utilities.timestamp_model import TimeStampModel


class Soup(TimeStampModel):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(blank=True, max_length=50, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Soup"
        verbose_name_plural = "Soups"


class Picture(TimeStampModel):
    soup = models.ForeignKey('Soup', on_delete=models.CASCADE, related_name='soup_image')
    image = models.FileField(upload_to='images/', validators=[validate_file_type])
