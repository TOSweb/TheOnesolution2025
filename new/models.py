from django.db import models

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=200)
    meta_description = models.TextField()
    meta_keywords = models.TextField()
    heading = models.CharField(max_length=300)
    small_description = models.TextField()
    schema = models.JSONField()
    project_completed = models.IntegerField()
    client_retention = models.IntegerField()
    years_of_experience = models.IntegerField()


    def __str__(self):
        return self.heading
    

    
