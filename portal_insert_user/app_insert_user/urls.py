from django.urls import path

# Import views
from . import views

app_name = "app_insert_user"

urlpatterns = [
   path("", views.home, name="index"),
   path('appointments/login.html', views.form, name='login'),  # Rota para appointments/form
]