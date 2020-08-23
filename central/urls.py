from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('contributors/', TemplateView.as_view(template_name='dev.html'), name='dev'),
    path('stats/general/', views.GenStats_View.as_view(), name='gstats'),
    path('add/',views.newdt,name='add'),
    path('details/',views.H_Details.as_view(), name='details'),
    path('research/data/',views.Fetchdata, name='data'),
    path('change/',views.Details_change.as_view(), name='change'),
    path('records/all/', views.AllRecords.as_view(), name='all_records'),
    path('random/', views.random_gen, name='random'),
    path('add_request/', views.Add_Request.as_view(), name='add_req'),
    path('requests/all/', views.All_Requests.as_view(), name='all_req'),
    path('requests/<pk>/', views.ReqDetailView.as_view(), name='req_detail'),
    path('generate/', TemplateView.as_view(template_name='generate.html'), name='generate'),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('manifest.json',TemplateView.as_view(template_name='pwa/manifest.json',content_type='text/plain')),
    path('serviceworker.js',TemplateView.as_view(template_name='pwa/serviceworker.js',content_type='text/javascript')),
]