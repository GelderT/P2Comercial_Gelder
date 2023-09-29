from django.urls import path
from . import views  # Asegúrate de importar tus vistas desde el archivo views.py

app_name = 'miapp'

urlpatterns = [
    path('orden/', views.OrdenesView.as_view(), name='orden-list'),
    path('orden/<int:id>/', views.OrdenesView.as_view(), name='orden-detail'),
    
]


