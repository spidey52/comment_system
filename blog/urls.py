from django.urls import path
from .views import post_list, post_detail, PostListView, test_one

app_name = 'blog'

urlpatterns = [
	# path('', post_list, name='post_list' ),
	path('', PostListView.as_view(), name='post_list'),
	path('test/', test_one, name='testing'),
	path('<slug:post>/', post_detail, name='post_detail' ),
]