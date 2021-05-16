from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('registerPage', views.regPage),
    path('login', views.login),
    path('register', views.register),
    path('dashboard', views.dashboard),
    path('dashboard/<str:category>', views.category),
    path('logout', views.logout),
    path('newWorkout', views.newWorkout),
    path('add', views.add),
    path('edit/<int:workout_id>', views.edit),
    path('update/<int:workout_id>', views.update),
    path('destroy/<int:workout_id>', views.delete)
]
