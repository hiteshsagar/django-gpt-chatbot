from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.chatbot, name='chatbot'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
=======
    # path('admin/', admin.site.urls),
    path('', views.chatbot, name='chatbot')
>>>>>>> 8b0375ea12985bab33a155b15927a0ed40954fbb
]