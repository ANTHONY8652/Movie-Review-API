from rest_framework import serializers
from .models import Review
from .utils import fetch_movie_details

class ReviewSerializer(serializers.ModelSerializer):
    movie_details = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'movie_title', 'review_content', 'rating', 'user','created_at', 'movie_details']
        read_only_fields = ['id', 'user', 'created_at']

        def validate_rating(self, value):
            if not (1 <= value <= 5):
                raise serializers.ValidationError('Rating must be between 1 and 5.')
            return value
        
        def get_movie_details(self, obj):
            return fetch_movie_details(obj.movie_title)