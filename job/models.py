from django.db import models

# Create your models here.

Job_Type = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

# Help function to upload images
def image_upload(instance, imagename_with_extension):
    imagename, extension = imagename_with_extension.split(".") # split the image file that upload
    return "jobs/%s.%s"%(instance.id, extension)

class Job(models.Model):
    title = models.CharField(max_length=100)
    # location =
    job_type = models.CharField(max_length=15, choices=Job_Type)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)

    def __str__(self):
       return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name