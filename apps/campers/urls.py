from django.conf.urls.defaults import patterns, url
from apps.campers.forms import RegistrationView

urlpatterns = patterns('',
        url(r'register/$',
                RegistrationView.as_view(),
                name='register'),
)
