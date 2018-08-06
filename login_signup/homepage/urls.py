
from . import views
from django.urls import include,path


app_name='homepage'
urlpatterns = [

    path('signup/', views.signup, name='signup'),

    path('',views.login_view,name="login_view"),

]

