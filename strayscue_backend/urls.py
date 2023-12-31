"""strayscue_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header="Strayscue Administration"
admin.site.site_title="Strayscue Administration"
admin.site.index_title="Welcome to Administration Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authorize/', include('authorization.urls')),
    path('sponsors/', include('sponsor_management.urls')),
    path('vets/', include('vet_management.urls')),
    path('reporters/', include('reporter_management.urls')),
    path('ngos/', include('ngo_management.urls')),
    path('cases/', include('case_management.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)