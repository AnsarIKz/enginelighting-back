from django.urls import path, include
from .views import PostList, PostDetail, ReviewListView, ProjectList, ProjectDetail, UsefulList, UsefulDetail, CreateRequest, CategoryList, CatalogList, CategoryParentsView, ProductDetail, ProductList

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
    path('catalog/<int:pk>/parents/',
         CategoryParentsView.as_view(), name='category-parents'),

    path("product/", ProductList.as_view(), name=""),
    path("product/<int:pk>/", ProductDetail.as_view()),


]
