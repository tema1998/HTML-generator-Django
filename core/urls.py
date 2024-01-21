from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('start-project', views.StartProject.as_view(), name='start-project'),
    path('process/<int:result_id>/', views.Process.as_view(), name='process'),
    ]