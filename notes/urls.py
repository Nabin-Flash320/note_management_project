
from django.urls import path
from . import views

# This is the notes app's URL pattern.
# IT maps all the functionalities of the app.
urlpatterns = [
   path('/', views.notes_listing, name='notes_listing'),
   path('/add', views.notes_adding, name='notes_adding'),
   path('/delete', views.notes_deleting, name='notes_deleting') 
]



