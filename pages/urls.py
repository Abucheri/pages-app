from django.urls import path
from .views import *  # import our homepage view

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),  # When using Class-Based Views, you always add as_view() at the end of the view name
	path('about/', AboutPageView.as_view(), name='about'),
]