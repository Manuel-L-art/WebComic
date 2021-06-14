from django.db import models

class Comic(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    release_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated_on = models.DateTimeField(auto_now=True)

class comicPage(models.Model):
    comicOrigin = models.ForeignKey(Comic, related_name="comic_page")
    imgfile = models.ImageField(upload_to="Comic", height_field=1035, width_field=800, max_length=350)
    uploaded_on = models.DateTimeField(auto_now_add=True)

