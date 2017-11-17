from django.conf.urls import url, include
# from django.contrib import admin
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static
from Patient import views


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^', views.HomeView.as_view()),
 ]