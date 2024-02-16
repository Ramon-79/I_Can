from django.urls import path
from blog import views
from . import views, api

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:pk>-<str:slug>/', views.category_page, name='category_page'),
]

# Паттерны API
urlpatterns += [
    path('bot/get-file/', api.GetFilePath.as_view()),
    path('bot/create-user/', api.CreateBotUser.as_view()),
]
