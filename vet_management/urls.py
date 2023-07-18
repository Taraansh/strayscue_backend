from django.urls import path
from vet_management import views

urlpatterns = [
    path('upload-vet/', views.upload_vet, name='upload-vet'),
    path('all/', views.get_all_vets, name='get-all-vets'),
    path('vet/<str:vet_name>/', views.search_vet, name='search-vet'),
    path('vet/update/<int:id>/', views.update_vet, name='update-vet'),
    path('vet/delete/<int:id>/', views.delete_vet, name='delete-vet'),
]
