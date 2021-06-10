
from django.urls import path
from .views import HomePageView, PostDetailView, AddPostView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>',PostDetailView.as_view(), name='detail'),
    path('post/',AddPostView.as_view(), name='post'),
]

