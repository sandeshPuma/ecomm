from django.contrib import admin
from django.urls import path
from . import views  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('about/', views.about, name='about'),# Add this line to map the root URL to a view
    path('register/', views.register_user, name='register'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>/', views.category, name='category'),
    
]
