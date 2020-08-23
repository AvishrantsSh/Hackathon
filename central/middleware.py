from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.contrib.auth import get_user_model

User=get_user_model()


EXEMPT_URLS = ("/",
                "/accounts/login/",
                "/accounts/logout/",
                "/contributors/",
                "/stats/general/",
                "/add/",
                '/research/data/',
                '/generate/',
                "/manifest.json",
                "/serviceworker.js",
                "/robots.txt"
                )

SUPER_URLS = ("manage","detail")
class AuthRequired(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
            assert hasattr(request, 'user')
            path = request.path_info
            
            if not request.user.is_authenticated and str(path) not in EXEMPT_URLS:
                return HttpResponseRedirect(reverse('login')+'?next='+request.path) # or http response
            return None

class SuperOnly(MiddlewareMixin):
    
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
            assert hasattr(request, 'user')
            path = request.path_info.split('/')[1]
            if request.user.is_authenticated:
                if not (request.user.is_superuser or User.objects.get(username = request.user.username).is_admin) and str(path) in SUPER_URLS:
                    return HttpResponseRedirect(reverse('home'))
            return
            