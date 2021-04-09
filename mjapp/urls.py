from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name="mjapp/login.html", success_url="/"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('purchase/', views.purchase, name="purchase"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('service/', views.service, name="service"),
    path('booking/', views.booking, name="booking"),
    path('booking/<int:id>/complete/', views.markComplete, name="markComplete"),
    path('services-completed/', views.serviceOffered, name="serviceOffered"),
    path('services-completed/<int:id>/payed/', views.markPayed, name="markPayed"),
]
