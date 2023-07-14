from django.urls import path
from sponsor_management import views


urlpatterns = [
    path('upload-sponsor/', views.upload_sponsor, name='upload-sponsor'),
    path('all/', views.get_all_sponsors, name='get-all-sponsors'),
    path('sponsor/<str:sponsor_name>/', views.search_sponsor, name='search-sponsor'),
]
