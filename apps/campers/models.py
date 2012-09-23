from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Camper(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=32, blank=True)
    info = models.TextField()
    phone = models.CharField(max_length=32, blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return unicode(self.user.username)
