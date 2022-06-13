from django.urls import path
from .api import ItemList

urlpatterns = [
    path('items/', ItemList.as_view(), name='items_list')
]
