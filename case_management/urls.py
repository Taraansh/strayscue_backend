from django.urls import path
from case_management import views

urlpatterns = [
    path('allcases/<str:email>/', views.get_cases_by_email, name='get_cases_by_email'),
    path('add/', views.create_case, name='case-create'),
    path('update/<int:case_id>/', views.update_case, name='case-update'),
    path('delete/<int:case_id>/', views.delete_case, name='case-delete'),
    
    path('addreporter/', views.create_case_reporter, name='create_case_reporter'),
    path('addanimal/', views.create_case_animal, name='create_case_animal'),
    path('addmedical/', views.create_case_medical_details, name='create_case_medical'),
    path('addoperational/', views.create_case_operation_details, name='create_case_medical'),
    path('addpostop/', views.create_case_post_operation_details, name='create_case_post_operation_details'),


    # path('updatereporter/<int:case_id>/', views.update_case, name='case-update'),
    # path('deletereporter/<int:case_id>/', views.delete_case, name='case-delete'),
]
