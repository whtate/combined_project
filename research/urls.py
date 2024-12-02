from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Import the auth views
from myapp import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('register/', user_views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Add login view
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Redirect to homepage after logout
    path('', user_views.map_view, name='home'),  # Add this line for the root path
]
