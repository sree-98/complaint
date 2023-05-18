"""complaintbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first),
    path('index', views.index),
    path('userregister',views.userregister),
    path('complaint', views.complaint),
    path('viewuserregister', views.viewuserregister),
    path('viewcomplaint', views.viewcomplaint),
    path('viewcomplaintadmin', views.viewcomplaintadmin),
    path('viewcomplaintHr', views.viewcomplaintHr),
    path('viewcomplaintTrainer', views.viewcomplaintTrainer),
    path('viewcomplaintOperationshead', views.viewcomplaintOperationshead),
    path('facregister', views.facregister),
    path('viewfacregister', views.viewfacregister),
    path('acknowledgement', views.acknowledgement),
    path('facacknowledgement', views.facacknowledgement),
    path('viewacknowledgement', views.viewacknowledgement),
    path('viewfacacknowledgement', views.viewfacacknowledgement),
    path('viewfacacknowledgementTrainer', views.viewfacacknowledgementTrainer),
    path('viewfacacknowledgementHr', views.viewfacacknowledgementHr),
    path('viewfacacknowledgementOperationshead', views.viewfacacknowledgementOperationshead),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('studentlogin', views.studentlogin, name='studentlogin'),
    path('facultylogin', views.facultylogin, name='facultylogin'),
    path('logout', views.logout),
    path('studentprofile', views.studentprofile),
    path('adminprofile', views.adminprofile, name='adminprofile'),
    path('facultyprofile', views.facultyprofile),
    path('update/<int:id>', views.update, name= 'update'),
    path('update/update1/<int:id>', views.update1, name= 'update1'),
    path('updates/<int:id>', views.updates, name='updates'),
    path('updates/updates1/<int:id>', views.updates1, name= 'updates1'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('deletee/<int:id>', views.deletee, name='deletee'),
    path('userupdate/<int:id>', views.userupdate, name= 'userupdate'),
    path('userupdate/edituserprofile/<int:id>', views.edituserprofile, name='edituserprofile'),
    path('update1', views.update1, name= 'update1'),
    path('log', views.log),
  
    
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
