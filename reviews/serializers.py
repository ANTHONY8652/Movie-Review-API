from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'movie_title', 'review_content', 'rating', 'user','created_at']
        read_only_fields = ['id', 'user', 'created_at']

        def validate_rating(self, value):
            if not (1 <= value <= 5):
                raise serializers.ValidationError('Rating must be between 1 and 5.')
            return value