from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.register, name='registration'),
    path('fancy_forms/', views.fancy_forms, name='fancy'),
    path('logout/', views.user_logout, name='logout'),
    path('user_login/', views.user_login, name='login'),
    # USING THE REVERSE FUNCION IN VIEWS.PY SPARES YOU ALL OF THAT:
    # setting up the page URL for the logged in user
    # path('user_login/index/', views.index, name='index'),
    # path('user_login/special/', views.special, name='special'),
    # # setting up the page URL for the logged in user
    # path('logout/index/', views.index, name='index'),
]