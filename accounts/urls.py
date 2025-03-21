from django.urls import path,include
from .views import SignUpView
urlpatterns=[
    path('singup/',SignUpView.as_view(),name='signup'),
]