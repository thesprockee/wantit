from django.conf.urls.defaults import patterns, url
from apps.campers.forms import RegistrationView
from django.contrib.auth.views import logout, login
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = patterns('',
        url(r'register/$',
                RegistrationView.as_view(),
                name='register'),
        url(r'logout/$', logout, {'next_page': '/'}, name='logout'),
        url(r'login/$', login, {'template_name': 'login.html'}, name='login'),
)
