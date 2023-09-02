from django.urls import *
from .views import *
urlpatterns = [
    path('' , HomePageView.as_view(),name='home' ), 
    path ('aboutus' , AbutUsView.as_view() , name = 'abut_us')
]