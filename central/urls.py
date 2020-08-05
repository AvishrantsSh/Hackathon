from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('add/',views.newdt,name='add'),
    path('random/', views.random_gen, name='random')
    # path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    # path('manifest.json',TemplateView.as_view(template_name='pwa/manifest.json',content_type='text/plain')),
    # path('serviceworker.js',TemplateView.as_view(template_name='pwa/serviceworker.js',content_type='text/javascript')),
]