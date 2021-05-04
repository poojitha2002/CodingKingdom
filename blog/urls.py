from django.conf.urls import url
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    resourcesView,
    KLHub

)
from . import views

urlpatterns = [
    path('discussionforum/', PostListView.as_view(), name='blog-home'),
url(r'^user/(?P<username>\w{0,50})/$', UserPostListView.as_view(), name='user-posts'),

    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('',views.homepage,name='homepage'),

    path('mockInterviews/', views.mock, name='mock'),
    path('courses/', views.courses, name='courses'),
    path('paint/', views.paint, name='paint'),
    path('contact/',views.contact,name='contact'),
    path('success/',views.successView,name='success'),
    path('resources/', resourcesView.as_view(), name='resources'),
    path('download/', views.download_file,name='download_file'),
    path('downloadpdf/', views.download_pdf_file, name='download_pdf_file'),

    path('KL-Hub/', KLHub.as_view(), name='klu'),
]
