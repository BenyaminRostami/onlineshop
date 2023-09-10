from django.urls import path 
from .views import *
urlpatterns = [ 
    path ("signup/" , SignupViews.as_view() , name="signup")
]