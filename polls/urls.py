from django.urls import path

from polls.views import IndexView, QuestionDetail, vote, ResultsView

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path('<int:pk>/', QuestionDetail.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
]