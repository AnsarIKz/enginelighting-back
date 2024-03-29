from rest_framework.views import APIView
from .models import Category
from rest_framework.response import Response
from django.http import Http404
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Post, Review, Useful, Project, Category, Product
from .serializers import PostSerializer, ReviewSerializer, UsefulSerializer, ProjectSerializer, CategorySerializer, RequestSerializer, ProductSerializer
import telebot

bot = telebot.TeleBot(token='5803280798:AAG1llHaBuRg5IrKK6foV15ZQmlXQKEFURk')
chat_id = '-967463798'


def send_telegram_message(message):
    bot.send_message(chat_id=chat_id, text=message)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UsefulList(generics.ListAPIView):
    queryset = Useful.objects.all()
    serializer_class = UsefulSerializer


class UsefulDetail(generics.RetrieveAPIView):
    queryset = Useful.objects.all()
    serializer_class = UsefulSerializer


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CreateRequest(generics.CreateAPIView):
    serializer_class = RequestSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        instance = response.data
        message = f'New request:\nFull name: {instance["full_name"]}\nPhone: {instance["phone"]}\nAdditional text: {instance["additional_text"]}'
        send_telegram_message(message)
        return response


# CATALOG

class CatalogList(generics.ListAPIView):
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = Category.objects.filter(parent=pk)
        if not queryset:
            queryset = Product.objects.filter(category=pk)
        return queryset

    def get_serializer_class(self):
        if Category.objects.filter(parent=self.kwargs.get('pk')).exists():
            return CategorySerializer
        else:
            return ProductSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer


class CategoryParentsView(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(id=pk)
            parents = self.get_all_parents(category)
            parent_names = [{'name': parent.name, 'id': parent.id}
                            for parent in parents]
            parent_names.insert(0, {'name': category.name, 'id': category.id})
            return Response(parent_names)
        except Category.DoesNotExist:
            return Response({'error': 'Category does not exist'})

    def get_all_parents(self, category):
        parents = []
        if category.parent is not None:
            parents.append(category.parent)
            parents += self.get_all_parents(category.parent)
        return parents


class ProductList(generics.ListAPIView):
    queryset = Product.objects.order_by('id')[:10]
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
