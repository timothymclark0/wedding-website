from django.db import models
from PIL import Image
# Create your models here.

class Photo(models.Model):
    name = models.CharField(blank=True, null=True, max_length=255)
    file = models.FileField()
    thumbnail = models.FileField(null=True,blank=True)
    height = models.IntegerField(null=True,blank=True)
    width = models.IntegerField(null=True,blank=True)
    
    def create_thumbnail(self):
        if self.file:
            img = Image.open(self.file)
            img.thumbnail((512,512))
            outpath = img.save(self.file.path.split('.')[0]+'_thumb.'+self.file.path.split('.')[-1])
            self.thumbnail = self.file.path.split('.')[0]+'_thumb.'+self.file.path.split('.')[-1]
            self.save()
        return self.thumbnail
    def height_and_width(self):
        img = Image.open(self.file)
        self.width, self.height = img.size
        self.save()
        return self
    def __str__(self):
        return self.name if self.name else f"Photo {self.pk}"
        
        
