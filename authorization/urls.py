from django.urls import path
from authorization import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', views.login, name='login'),
    path('routes/', views.get_routes),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('passchange/<str:email>/', views.password_change, name='change_password'),
    path('update/<str:email>/', views.update_profile, name="update_profile"),
    path('modify/<int:id>/', views.update_profile_via_ngo_profile, name="update_profile_via_ngo_profile"),
    path('getprofile/<str:email>/', views.get_profile, name="get_profile" ),
    path('signup/', views.signup, name='signup'),
    path('getallusers/', views.get_all_users, name='get_all_users'),
]
