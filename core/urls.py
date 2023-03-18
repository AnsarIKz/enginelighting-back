from django.urls import path, include
from .views import PostList, PostDetail, ReviewListView, ProjectList, ProjectDetail, UsefulList, UsefulDetail, CreateRequest, CategoryList, CatalogList

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),

    path("project/", ProjectList.as_view()),
    path("project/<int:pk>/", ProjectDetail.as_view()),

    path("useful/", UsefulList.as_view()),
    path("useful/<int:pk>/", UsefulDetail.as_view()),

    path('reviews/', ReviewListView.as_view()),

    path('requests/create/', CreateRequest.as_view(), name='create-request'),

    # CATALOG

    path("catalog/", CategoryList.as_view()),
    path("catalog/<int:pk>/", CatalogList.as_view()),

]
