from django.urls import path 
from . import views

urlpatterns = [
    path('',views.Portfolio,name="portfolio"),
    path('djangoprojects/',views.DjangoProjects,name="djangoprojects"),
    path('contact/',views.Contact,name="contact"),
    
]
