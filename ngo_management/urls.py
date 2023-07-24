from django.urls import path
from ngo_management import views


urlpatterns = [
    path('all/<str:email>/', views.get_all_ngos, name='get_all_ngos'),
    path('addngo/', views.add_ngo, name='add_ngo'),
    path('delete/<int:id>/', views.delete_ngo, name='delete_ngo'),
    path('update/<int:id>/', views.update_ngo, name='update_ngo'),
]
