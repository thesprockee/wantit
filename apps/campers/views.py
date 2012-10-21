# Create your views here.
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.db.models import Q

class CamperList(ListView):
    template_name = "campers/camper_list.html"
    search_fields = ('email', 'username', 'camper__nickname')

    def get_queryset(self):
        search_string = self.request.GET.get('search_string', None)
        if search_string:
            query = None
            for f in self.search_fields:
                q = Q(**{f + "__icontains": search_string})
                if not query:
                    query = q
                else:
                    query = query | q
            return User.objects.filter(query)
        return User.objects.all()
