#기본 path 함수를 사용하기 위해 똑같이 해당 기능을 import
# 프로젝트에서는 어떤 app의 views인지 알기 위해 blog.views 앱부터 명시했지만
# 여기에서는 동일한 폴더 내에 잇는 views라는 것을 명시하기 위해 
# from .(현재폴더) import views 로 사용한다.

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:post_id>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/delete/', views.delete, name="delete"),
    path('<int:post_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:post_id>/comments/<int:comment_id>/update/', views.comments_update, name='comments_update'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)