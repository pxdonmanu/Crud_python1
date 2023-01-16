from django.urls import path 
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns=[
    path('', views.start, name='index'),
    path('us', views.us, name='us'),
    path('products', views.products, name='products'),
    path('products/create', views.create, name='create'),
    path('products/edit', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('products/edit/<int:id>', views.edit, name='edit')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
