from django.urls import path


from gestion import views


urlpatterns = [
   path('', views.index, name='index'),
   path('insert/', views.departamentos, name='departamentos'),


]

