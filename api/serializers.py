from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    #model Seilaizer
    class Meta:
        model = Article
        fields = ['id','title','desc']

    #serializer
    # title = serializers.CharField(max_length=100)
    # desc = serializers.CharField(max_length=800)
    #
    # def create(self, validated_data):
    #     return Article.objects.create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.desc = validated_data.get('desc', instance.desc)
    #     return Article.objects.update()