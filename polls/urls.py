from django.urls import path

from polls.views import index, detail

urlpatterns = [
    path("", index, name="home"),
    path('<int:question_id>/', detail, name='detail'),
]