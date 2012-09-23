from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import transaction
from autoslug import AutoSlugField

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=64)
    slug = AutoSlugField(populate_from='title')

    def __unicode__(self):
        return unicode(self.title)


class Message(models.Model):
    topic = models.ForeignKey(Topic)
    author = models.ForeignKey(User)
    created = models.DateTimeField(default=timezone.now, editable=False)
    body = models.TextField(blank=False)

    def __unicode__(self):
        return unicode("%s: %s" % (self.author, self.topic))

    @staticmethod
    def create(author, body, topic):
        with transaction.commit_on_success():
            topic_obj, created = Topic.objects.get_or_create(title=topic)
            if created:
                topic_obj.save()
            message = Message(topic=topic_obj, author=author, body=body)
            message.save()
        return message

    @property
    def last_change(self):
        try:
            return self.history.latest('timestamp')
        except MessageHistory.DoesNotExist:
            return None


class MessageHistory(models.Model):
    message = models.ForeignKey(Message, related_name='history')
    editor = models.ForeignKey(User)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)

    def __unicode__(self):
        return unicode("[%s] %s: %s" % (timestamp, editor, message))


class TopicTracker(models.Model):
    topic = models.ForeignKey(Topic)
    user = models.ForeignKey(User)
    last_read = models.ForeignKey(Message)
    subscribed = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode("%s: %s" % (user, topic))
