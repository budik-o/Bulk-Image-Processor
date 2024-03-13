from django.db import models

class ImageModel(models.Model):
    image = models.FileField(upload_to = "results/")
    filename = models.CharField(max_length = 100, null = True, blank = True)
    file_extension = models.CharField(max_length = 20, null = True, blank = True)
        
class ModificationModel(models.Model):
    filter_type = models.CharField(max_length = 20, null = True, blank = True)
    adjustment_type = models.CharField(max_length = 20, null = True, blank = True)
    factor = models.FloatField(null = True, blank = True)
