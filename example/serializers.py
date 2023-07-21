from rest_framework import serializers
from .models import Book


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['bid', 'title', 'author', 'category', 'pages', 'price', 'published_date', 'description']

#
# class BookSerializers(serializers.Serializer):
#     bid = serializers.IntegerField(primary_key=True) # 책 id
#     title = serializers.CharField(max_length=50)     # 책 제목
#     author = serializers.CharField(max_length=50)    # 저자
#     category = serializers.CharField(max_length=50)    # 페이지 수
#     pages = serializers.IntegerField()    # 카테고리
#     price = serializers.IntegerField()    # 가격
#     published_date = serializers.DateField()    # 출판일
#     description = serializers.TextField()    # 도서설명
#
#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.bid = validated_data.get('bid', instance.bid)
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.category = validated_data.get('category', instance.category)
#         instance.pages = validated_data.get('pages', instance.pages)
#         instance.price = validated_data.get('price', instance.price)
#         instance.published_date = validated_data.get('published_date', instance.published_date)
#         instance.description = validated_data.get('description', instance.description)
#         instance.save()
#
#         return instance
#
