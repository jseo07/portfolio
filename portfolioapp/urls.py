from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path("", views.index, name="index"),
    path('contact/', views.contact_view, name='contact'),
    path('under-construction/', views.under_construction, name='under-construction'),
    path('post-lstm/', views.lstm, name='post-lstm'),
    path('gmci/', views.gmci, name='gmci'),
]