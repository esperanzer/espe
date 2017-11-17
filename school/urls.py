"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from Admission import views
from Appointment import views
from Doctor import views as docView
from Patient import views
from Treatment import views
from User import views
from Ward import views
from Login import views
from Signout import views
from home.views import index as home_view




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_view, name='home'),
    url(r'^Admission/', include('Admission.urls')),
    url(r'^Appointment/', include('Appointment.urls')),
    url(r'^Doctor/', docView.HomeView, name='doctor'),
    url(r'^Patient/', include('Patient.urls')),
    url(r'^Treatment/', include('Appointment.urls')),
    url(r'^User/', include('User.urls')),
    url(r'^Ward/', include('Ward.urls')),
    url(r'^Login/', include('Login.urls')),
    url(r'^Signout/', include('Signout.urls')),
]


'''
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC)
'''
    #what if l rite this not the above?
 #+ static(settings.STATIC_URL,
#document_root=settings.STATIC_ROOT)





