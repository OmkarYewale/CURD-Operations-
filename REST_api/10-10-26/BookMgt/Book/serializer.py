from rest_framework import serializers
from .models import Book

class BookSerialize(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    author = serializers.CharField(max_length=100)
    stock_count = serializers.IntegerField(min_value=0)
    is_available = serializers.BooleanField(default=True)

    def validate(self, data):
        if data.get("stock_count")==0:
            data["is_available"]=False

        return data

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get(
            "title",instance.title
        )

        instance.author = validated_data.get(
            "author",instance.author
        )

        instance.stock_count = validated_data.get(
            "stock_count",instance.stock_count
        )

        instance.is_available = validated_data.get(
            "is_available",instance.is_available
        )

        instance.save()

        return instance