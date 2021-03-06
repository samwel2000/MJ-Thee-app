from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('', views.index, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name="mjapp/login.html", success_url="/"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('purchase/', views.purchase, name="purchase"),
    path('', views.dashboard, name="home"),
    path('service/', views.service, name="service"),
    path('service/<int:id>/update/', views.editService, name="editService"),
    path('service/<int:id>/delete/', views.deleteService, name="deleteService"),
    path('booking/', views.booking, name="booking"),
    path('booking/<int:id>/edit/', views.editBooking, name="editBooking"),
    path('booking/<int:id>/cancel/', views.cancelBooking, name="cancelBooking"),
    path('booking/<int:id>/complete/', views.markComplete, name="markComplete"),
    path('services-completed/', views.serviceOffered, name="serviceOffered"),
    path('services-completed/<int:id>/payed/', views.markPayed, name="markPayed"),
]
