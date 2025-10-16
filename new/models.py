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
    no_of_clients = models.IntegerField()
    years_of_experience = models.IntegerField()
    og_title = models.TextField()
    og_type = models.TextField()
    og_url = models.TextField()
    og_image = models.TextField()
    og_description = models.TextField()
    og_site_name = models.TextField()
    canonical_url = models.URLField(blank=True, null=True, help_text="Preferred URL for this page")

    def __str__(self):
        return self.heading

class AlternateHome(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    rel = models.CharField(max_length=200, null=True, blank=True)
    link = models.URLField()

    def __str__(self):
        return self.link

class About(models.Model):
    heading = models.CharField(max_length=300)
    image_m = models.ImageField(upload_to='image_m/')
    image_t = models.ImageField(upload_to='image_t/')
    image_d = models.ImageField(upload_to='image_d/')
    alt = models.CharField(max_length=1000)
    small_description = models.TextField()
    content = models.TextField()
    vision = models.TextField()
    mission = models.TextField()

    #SEO
    title = models.CharField(max_length=200)
    meta_description = models.TextField()
    meta_keywords = models.TextField()
    schema = models.JSONField()
    og_title = models.TextField()
    og_type = models.TextField()
    og_url = models.TextField()
    og_image = models.TextField()
    og_description = models.TextField()
    og_site_name = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.heading
    
class ServiceCategory(models.Model):
    heading = models.CharField(max_length=300)
    image_m = models.ImageField(upload_to='image_m/')
    image_t = models.ImageField(upload_to='image_t/')
    image_d = models.ImageField(upload_to='image_d/')
    alt = models.CharField(max_length=1000)
    small_description = models.TextField()
    content = models.TextField()
    #SEO
    title = models.CharField(max_length=200)
    meta_description = models.TextField()
    meta_keywords = models.TextField()
    schema = models.JSONField()
    og_title = models.TextField()
    og_type = models.TextField()
    og_url = models.TextField()
    og_image = models.TextField()
    og_description = models.TextField()
    og_site_name = models.TextField()
    slug = models.SlugField(unique=True)
    
    def __str__(self):

        return self.heading
    
class ServiceCategoryContent(models.Model):
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    image_m = models.ImageField(upload_to='image_m/', blank=True)
    image_t = models.ImageField(upload_to='image_t/', blank=True)
    image_d = models.ImageField(upload_to='image_d/', blank=True)
    content = models.TextField(blank=True)
    youtube_video_embed = models.URLField(blank=True)

class Service(models.Model):
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    heading = models.CharField(max_length=300)
    image_m = models.ImageField(upload_to='image_m/')
    image_t = models.ImageField(upload_to='image_t/')
    image_d = models.ImageField(upload_to='image_d/')
    alt = models.CharField(max_length=1000)
    small_description = models.TextField()
    content = models.TextField()
    #SEO
    title = models.CharField(max_length=200)
    meta_description = models.TextField()
    meta_keywords = models.TextField()
    schema = models.JSONField()
    og_title = models.TextField()
    og_type = models.TextField()
    og_url = models.TextField()
    og_image = models.TextField()
    og_description = models.TextField()
    og_site_name = models.TextField()
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.heading

class ServiceContent(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    image_m = models.ImageField(upload_to='image_m/', blank=True)
    image_t = models.ImageField(upload_to='image_t/', blank=True)
    image_d = models.ImageField(upload_to='image_d/', blank=True)
    content = models.TextField(blank=True)
    youtube_video_embed = models.URLField(blank=True)



class ServiceVariant(models.Model):
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    heading = models.CharField(max_length=300)
    image_m = models.ImageField(upload_to='image_m/')
    image_t = models.ImageField(upload_to='image_t/')
    image_d = models.ImageField(upload_to='image_d/')
    alt = models.CharField(max_length=1000)
    small_description = models.TextField()
    content = models.TextField()
    #SEO
    title = models.CharField(max_length=200)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    schema = models.JSONField(blank=True, null=True)
    og_title = models.TextField(blank=True, null=True)
    og_type = models.TextField(blank=True, null=True)
    og_url = models.TextField(blank=True, null=True)
    og_image = models.TextField(blank=True, null=True)
    og_description = models.TextField(blank=True, null=True)
    og_site_name = models.TextField(blank=True, null=True)
    canonical_url = models.URLField(blank=True, null=True, help_text="Preferred URL for this page")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.heading

class ServiceVariantContent(models.Model):
    service_variant = models.ForeignKey(ServiceVariant, on_delete=models.CASCADE)
    image_m = models.ImageField(upload_to='image_m/', blank=True)
    image_t = models.ImageField(upload_to='image_t/', blank=True)
    image_d = models.ImageField(upload_to='image_d/', blank=True)
    content = models.TextField(blank=True)
    youtube_video_embed = models.URLField(blank=True)