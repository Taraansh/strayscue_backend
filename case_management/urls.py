from django.urls import path
from case_management import views

urlpatterns = [
    path('allcases/<str:email>/', views.get_cases_by_email, name='get_cases_by_email'),
    path('add/', views.create_case, name='case-create'),
    path('update/<int:case_id>/', views.update_case, name='case-update'),
    path('delete/<int:case_id>/', views.delete_case, name='case-delete'),

    path('ngocases/<str:email>/', views.get_cases_by_ngo, name='get_cases_by_ngo'),

    path('updatereporter/<int:id>/', views.update_reporter, name='report_update'),
    path('updateanimal/<int:id>/', views.update_animal, name='update_animal'),
    path('updatemedical/<int:id>/', views.update_medical, name='update_medical'),
    path('updateoperational/<int:id>/', views.update_operation, name='update_operation'),
    path('updatepostoperational/<int:id>/', views.update_post_operation, name='update_post_operation'),
]
