from django.db import models


# Create your models here.
class BoardMember(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    since = models.DateField()
    to = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    role = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['-first_name', '-last_name',]

    def __unicode__(self):
        return ' '.join([self.first_name, self.last_name,])

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])


class Matrikel(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['-name',]

    def __unicode__(self):
        return ' '.join([self.first_name, self.last_name,])

    def __str__(self):
        return self.name
