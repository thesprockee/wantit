from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Camper(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=32, blank=True)
    info = models.TextField()
    phone = models.CharField(max_length=32, blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return unicode(self.user.username)


class AccountRequest(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    info = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, editable=False)

    def __unicode__(self):
        return unicode(self.username)

    def approve(self):
        user = User.objects.create_user(username=self.username,
                email=self.email, password=self.password)
        user.save()
        camper = Camper(user=user, info=self.info)
        camper.save()
        self.delete()
        return user

    def deny(self):
        self.delete()
