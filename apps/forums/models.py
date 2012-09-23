from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.title)


class Message(models.Model):
    topic = models.ForeignKey(Topic)
    author = models.ForeignKey(User)
    created = models.DateTimeField(default=timezone.now, editable=False)
    body = models.TextField(blank=False)

    def __unicode__(self):
        return unicode("%s: %s" % (self.author, self.topic))

    @property
    def last_change(self):
        return self.history.latest('timestamp')


class MessageHistory(models.Model):
    message = models.ForeignKey(Message, related_name='history')
    editor = models.ForeignKey(User)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)

    def __unicode__(self):
        return unicode("[%s] %s: %s" % (timestamp, editor, message)


class TopicTracker(models.Model):
    topic = models.ForeignKey(Topic)
    user = models.ForeignKey(User)
    last_read = models.ForeignKey(Message)
    subscribed = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode("%s: %s" % (user, topic))
