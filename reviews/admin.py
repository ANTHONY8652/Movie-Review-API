from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['movie_title', 'review_content', 'rating', 'created_at', 'user']
    list_filter = ['movie_title', 'user']
    search_fields = ['movie_title', 'review_content', 'created_at', 'rating', 'user']
    date_hierarchy = 'created_at'

admin.site.register(Review, ReviewAdmin)

# Register your models here.
