from django.conf.urls.defaults import patterns, url
from apps.campers.forms import RegistrationView
from django.contrib.auth.views import logout, login
from django.contrib.auth.forms import AuthenticationForm
from apps.campers.views import CamperList
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
        url(r'register/$',
                RegistrationView.as_view(
                        template_name='campers/register.html'),
                name='register'),
        url(r'logout/$', logout, {'next_page': '/'}, name='logout'),
        url(r'login/$', login, {'template_name': 'campers/login.html'},
                name='login'),
        url(r'list/$', login_required(CamperList.as_view()),
                name='camper_list'),
)
