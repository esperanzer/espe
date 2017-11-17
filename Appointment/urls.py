from django.conf.urls import url, include
## Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static
from Appointment import views


urlpatterns = [
    # s
    url(r'^', views.HomeView.as_view()),
    ]

    