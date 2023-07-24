from django.urls import path
from reporter_management import views

urlpatterns = [
    path('all/<str:email>/', views.get_all_reporters, name='get_all_reporters'),
    path('addreporter/', views.add_reporter, name='add_reporter'),
    path('update/<int:id>/', views.update_reporter, name='update_reporter'),
    path('delete/<int:id>/', views.delete_reporter, name='delete_reporter'),
]
