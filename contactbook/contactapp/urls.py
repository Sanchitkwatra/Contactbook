from django.urls import path,include

from . import views

urlpatterns=[
    path('',views.ContactList.as_view()),
    path('<int:pk>/',views.ContactDetail.as_view()),
    path('login/',views.login),
    path('sampleapi/',views.sample_api),
]