from django.urls import path
from vet_management import views

urlpatterns = [
    path('all/<str:email>/', views.get_all_vets, name='get-all-vets'),
    path('addvet/', views.add_vet, name='add_vet'),
    path('delete/<int:id>/', views.delete_vet, name='delete-vet'),
    path('update/<int:id>/', views.update_vet, name='update-vet'),
]
