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
from django.conf import settings
from edc_base.views import LogoutView, LoginView
from edc_registration.admin_site import edc_registration_admin
from django.contrib import admin
from django.urls.conf import path, include
from django.views.generic.base import RedirectView

from .admin_site import bcpp_data_cleaning_admin
from .views import HomeView, AdministrationView

admin.autodiscover()

app_name = 'bcpp_data_cleaning'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('administration/', AdministrationView.as_view(),
         name='administration_url'),
    path('bcpp_data_cleaning_admin/', bcpp_data_cleaning_admin.urls),
    path('admin/', edc_registration_admin.urls),
    path('edc_registration/', include('edc_registration.urls')),
    path('edc_base/', include('edc_base.urls')),
    path('edc_device/', include('edc_device.urls')),
    path('tz_detect/', include('tz_detect.urls')),
    path('login', LoginView.as_view(), name='login_url'),
    path('accounts/login/', LoginView.as_view(), name='login_url'),
    # path(r'^accounts/login/', include('registration.backends.hmac.urls')),
    path('logout', LogoutView.as_view(
        pattern_name='login_url'), name='logout_url'),
    path('home/', HomeView.as_view(), name='home_url'),
    path('', HomeView.as_view(), name='home_url'),
]
