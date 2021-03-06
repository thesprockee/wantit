from django.contrib import admin
from apps.forums.models import Topic, Message, MessageHistory, TopicTracker

class BaseAdmin(admin.ModelAdmin):
    actions_on_top = True


class TopicAdmin(BaseAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Topic, TopicAdmin)


class MessageAdmin(BaseAdmin):
    list_display = ('author', 'topic', 'created')
    list_display_links = ('author', 'topic')
    list_filter = ('author',)
    search_fields = ('topic__title', 'body')
    date_hierarchy = 'created'


admin.site.register(Message, MessageAdmin)


class MessageHistoryAdmin(BaseAdmin):
    list_display = ('message', 'editor', 'timestamp')
    list_filter = ('editor',)
    search_fields = ('message__topic__title', 'message__body')
    date_hierarchy = 'timestamp'


admin.site.register(MessageHistory, MessageHistoryAdmin)


class TopicTrackerAdmin(BaseAdmin):
    list_display = ('topic', 'user', 'last_read', 'subscribed')
    list_filter = ('user',)
    search_fields = ('topic__title', 'message__body')


admin.site.register(TopicTracker, TopicTrackerAdmin)
