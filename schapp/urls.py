from django.urls import path
from . import views

app_name = 'schapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('departments/', views.departments, name='departments'),
    path('clubs/', views.clubs, name='clubs'),
    path('sports/', views.sports, name='sport'),
    path('send-message', views.MessageCreateView.as_view(), name='send-message'),
    path('<int:pk>/comment', views.CommentCreateView.as_view(), name='comment'),




]