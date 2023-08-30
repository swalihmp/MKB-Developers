from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views



urlpatterns = [
    path('AddProperty',views.AddProperty, name='AddProperty'),
    path('add_more',views.AddMore,name='add_more'),
    path('',views.HomePage,name='homepage'),
    path('add_image',views.Addimage,name='add_image'),
    path('add_data',views.Adddata,name='add_data'),
    path('change/<int:id>/<str:action>/',views.change,name='change'),
    path('singleprop/<int:id>/',views.Single,name='singleprop'),
    path('edit_data',views.EditData,name='edit_data'),
    path('remove_amenti/<int:id>/<int:id1>/',views.RemoveAmenti,name='remove_amenti'),
    path('enquiries',views.Enquiry,name='enquiries'),
    path('mark/<int:id>',views.Mark,name='mark'),
    path('login',views.Loginp,name='login'),
    path('logout',views.logout_p,name='logout')
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)