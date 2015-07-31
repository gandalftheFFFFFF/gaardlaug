from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField()
    published = models.BooleanField(default=True)
    slug = models.SlugField()

    class Meta:
        ordering = ['-date',]

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField(upload_to='images')
    post = models.ForeignKey(Post, blank=True, null=True)