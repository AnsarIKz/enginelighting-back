from django.http import Http404
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Post, Review, Useful, Project, Category
from .serializers import PostSerializer, ReviewSerializer, UsefulSerializer, ProjectSerializer, CategorySerializer, RequestSerializer


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

class CategoryChildList(generics.ListAPIView):

    serializer_class = CategorySerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Category.objects.filter(parent=pk)


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer
