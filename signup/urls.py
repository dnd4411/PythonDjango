from django.contrib import admin
from django.urls import path
from signup.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', user,name='signin'),
    path('login/', ulogin,name='login'),
    path('logout/', userlogout,name='logout'),
    path('reset/', reset_pw,name='reset'),
    path('newpassword/',  update_pa,name='newpassword'),
    path('conf_pw/',  conf_pw,name='conf_pw'),
     

]
