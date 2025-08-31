from django.db import models
from PIL import Image
from django.utils import timezone
# Create your models here.
class Gift(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length = 5000, null = True, blank = True)
    price = models.FloatField()
    price_range_low = models.FloatField(null=True, blank=True)
    price_range_high = models.FloatField(null = True, blank=True)
    url = models.URLField(null=True)
    thumbnail_base = models.FileField(null = True, blank=True)
    thumbnail = models.FileField(null=True, blank=True)
    slug = models.CharField(max_length=255)
    number_requested = models.IntegerField(default=1)

    def create_thumbnail(self):
        if self.file:
            img = Image.open(self.file)
            img.thumbnail((256,256))
            outpath = img.save(self.file.path.split('.')[0]+'_thumb.'+self.file.path.split('.')[-1])
            self.thumbnail = self.file.path.split('.')[0]+'_thumb.'+self.file.path.split('.')[-1]
            self.save()
        return self.thumbnail
    
    def __str__(self):
        return self.name
    
class Claim(models.Model):
    name = models.CharField(max_length=255)
    claimed_gift = models.ForeignKey(Gift, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    amount = models.FloatField(null=True, blank=True)
    time = models.DateTimeField(default = timezone.now)
    visible = models.BooleanField(default=True)
