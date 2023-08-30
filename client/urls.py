from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import Projects
from . import views



urlpatterns = [
    path('projects/',views.Projects, name='projects'),
    path('project_detals/<int:id>',views.Project_details,name='project_detals'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('save_data',views.Save_Data,name='save_data')
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)