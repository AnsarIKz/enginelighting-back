from .models import Review
from rest_framework import serializers
from .models import Post, PostPhoto, Useful, UsefulPhoto, Project, ProjectPhoto, Request, Category, Product


class PostPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPhoto
        fields = ('id', 'post', 'image', 'caption')


class PostSerializer(serializers.ModelSerializer):
    photos = PostPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'subtitle',
                  'created_at', 'updated_at', 'photos')


class UsefulPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulPhoto
        fields = ('id', 'post', 'image', 'caption')


class UsefulSerializer(serializers.ModelSerializer):
    photos = UsefulPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Useful
        fields = ('id', 'title', 'subtitle',
                  'created_at', 'updated_at', 'photos', 'file')


class ProjectPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPhoto
        fields = ('id', 'post', 'image', 'caption')


class ProjectSerializer(serializers.ModelSerializer):
    photos = ProjectPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'subtitle',
                  'created_at', 'updated_at', 'photos')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'image', 'created_at')


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        exclude = ()


# CATALOG

# class ChildCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id', 'name')


# class CategorySerializer(serializers.ModelSerializer):
#     children = ChildCategorySerializer(many=True)

#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'children')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')


class ProductSerializer(serializers.ModelSerializer):
    is_product = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_is_product(self, obj):
        return True

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['is_product'] = self.get_is_product(instance)
        return data
