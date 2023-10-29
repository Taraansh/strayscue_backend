from django.urls import path
from ngo_management import views


urlpatterns = [
    path('all/<str:email>/', views.get_all_ngos_using_email,
         name='get_all_ngos_using_email'),
    path('addngo/', views.add_ngo, name='add_ngo'),
    path('getngo/<int:id>/', views.get_ngo, name='get_ngo'),
    path('delete/<int:id>/', views.delete_ngo, name='delete_ngo'),
    path('update/<int:id>/', views.update_ngo, name='update_ngo'),
    path('allusers/<str:email>/', views.get_all_ngo_linked_user,
         name='get_all_ngo_linked_user'),
    path('allngos/', views.get_all_ngos, name="get_all_ngos"),
]
