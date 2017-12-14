"""edc_sync_file_monitor URL Configuration

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
from django.contrib import admin
from django.conf.urls import url, include
from edc_base.views import LogoutView, LoginView
from edc_registration.admin_site import edc_registration_admin

from .admin_site import bcpp_data_cleaning_admin
from .views import HomeView, AdministrationView


app_name = 'bcpp_data_cleaning'

admin.autodiscover()


urlpatterns = [
    url(r'^admin/edc_registration/', edc_registration_admin.urls),
    url(r'^edc_registration/',
        include('edc_registration.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^bcpp_data_cleaning_admin/', bcpp_data_cleaning_admin.urls),
    url(r'^admininistration/', AdministrationView.as_view(),
        name='administration_url'),
    url(r'^edc/', include('edc_base.urls')),
    url(r'login', LoginView.as_view(), name='login_url'),
    url(r'^tz_detect/', include('tz_detect.urls')),
    url(r'logout', LogoutView.as_view(
        pattern_name='login_url'), name='logout_url'),
    url(r'', HomeView.as_view(), name='home_url'),
]
