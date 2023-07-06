from django.urls import path
from .views import ProductApi

app_name = 'product'
urlpatterns = [
    path('', ProductApi.as_view(), name='create')
]
