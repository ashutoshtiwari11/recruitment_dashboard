from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.home ,name='home'), 
    path('signin/',views.handlesignin,name="signin"),
    path('login/',views.user_login, name="login"),
    path("logout/",views.user_logout, name='logout'),
    path('contact/',views.contact,name="contact"),
    path('hire/',views.hire, name = "checkout"),
    path('apply/',views.apply_job, name = "checkout"),
    path('track/', views.tracker,name="tracker"),
    path('search/',views.search,name="search"),
]