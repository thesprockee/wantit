from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import transaction
from autoslug import AutoSlugField
from difflib import unified_diff

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=64)
    slug = AutoSlugField(populate_from='title')
    locked = models.BooleanField(default=False)
    hidden = models.BooleanField(default=False)
    sticky = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.title)

    def get_unread_messages(self, user):
        tracker = TopicTracker.objects.get(topic=self, user=user)
        return Message.objects.filter(topic=self,
                id__gt=tracker.last_read.id)

    def unread_message_count(self, user):
        return self.get_unread_messages(user).count()


class Message(models.Model):
    topic = models.ForeignKey(Topic)
    author = models.ForeignKey(User)
    created = models.DateTimeField(default=timezone.now, editable=False)
    body = models.TextField(blank=False)

    def __unicode__(self):
        return unicode("%s: %s" % (self.author, self.topic))

    @staticmethod
    def create(author, body, topic, sticky=False):
        with transaction.commit_on_success():
            topic_obj, created = Topic.objects.get_or_create(title=topic,
                    defaults={'sticky': sticky})
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

    def edit(self, user, new_body):
        diff_obj = unified_diff(self.body.split('\n'), new_body.split('\n'),
                fromfile='old_body', tofile='new_body', lineterm='')
        diff = '\n'.join([l for l in diff_obj])
        with transaction.commit_on_success():
            history = MessageHistory(message=self, editor=user, diff=diff)
            history.save()
            self.body = new_body
            self.save()

    def has_read(self, user):
        """
        Returns True if the given user has already read this message.
        """
        tracker = TopicTracker.objects.get(topic=self.topic, user=user)
        return tracker.last_read.id >= self.id


class MessageHistory(models.Model):
    message = models.ForeignKey(Message, related_name='history')
    editor = models.ForeignKey(User)
    diff = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, editable=False)

    def __unicode__(self):
        return unicode("[%s] %s: %s" % (self.timestamp, self.editor,
                self.message))


class TopicTracker(models.Model):
    topic = models.ForeignKey(Topic)
    user = models.ForeignKey(User)
    last_read = models.ForeignKey(Message)
    subscribed = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode("%s: %s" % (self.user, self.topic))
