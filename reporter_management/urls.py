from django.urls import path
from reporter_management import views

urlpatterns = [
    path('upload-reporter/', views.upload_reporter, name='upload_reporter'),
    path('all/', views.get_all_reporters, name='get_all_reporters'),
    path('reporter/<str:vet_name>/', views.search_reporter, name='search_reporter'),
    path('reporter/update/<int:id>/', views.update_reporter, name='update_reporter'),
    path('reporter/delete/<int:id>/', views.delete_reporter, name='delete_reporter'),
]
