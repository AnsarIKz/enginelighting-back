from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Review, Useful, Project, Category
from .serializers import PostSerializer, ReviewSerializer, UsefulSerializer, ProjectSerializer, CategorySerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UsefulList(generics.ListCreateAPIView):
    queryset = Useful.objects.all()
    serializer_class = UsefulSerializer


class UsefulDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Useful.objects.all()
    serializer_class = UsefulSerializer


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CreateRequest(generics.CreateAPIView):
    serializer_class = RequestSerializer


# CATALOG

class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = RecursiveCategorySerializer

    def get_object(self):
        obj = super().get_object()
        return obj.children.all()


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer
