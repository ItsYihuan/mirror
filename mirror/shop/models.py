from django.db import models
from django.utils import timezone

# Create your models here.
class Cloth(models.Model):
    image = models.ImageField(upload_to='cloth/', blank=False, null=False)
    upload_date = models.DateField(default=timezone.now)

class Cloth_data(models.Model):
    image_ID = models.IntegerField(default=0)
    shoulder_s=models.IntegerField()
    shoulder_m=models.IntegerField()
    shoulder_l=models.IntegerField()
    shoulder_xl=models.IntegerField()
    shoulder_2l=models.IntegerField()

    chest_s=models.IntegerField()
    chest_m=models.IntegerField()
    chest_l=models.IntegerField()
    chest_xl=models.IntegerField()
    chest_2l=models.IntegerField()

    length_s=models.IntegerField()
    length_m=models.IntegerField()
    length_l=models.IntegerField()
    length_xl=models.IntegerField()
    length_2l=models.IntegerField()
    upload_date = models.DateField(default=timezone.now)
    def __int__(self):
        return self.image_ID
