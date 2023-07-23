from django.urls import path
from sponsor_management import views


urlpatterns = [
    path('all/<str:email>/', views.get_all_sponsors, name='get-all-sponsors'),
    path('addsponsor/', views.add_sponsor, name='add_sponsor'),
    path('delete/<int:id>/', views.delete_sponsor, name='delete-sponsor'),
    path('update/<int:id>/', views.update_sponsor, name='update-sponsor'),
]
