from django.urls import path
from . import views


app_name = 'survey' # 네임 스페이스 설정

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
