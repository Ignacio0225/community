from django.urls import path
from users import views

urlpatterns =[
    path('me/',views.User.as_view()),
    path('register/',views.CreateUser.as_view()),
    path('change-pw/',views.ChangeUserPassword.as_view()),

]