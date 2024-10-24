from django.db import models
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    movie_title = models.CharField(max_length=50)
    review_content = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie_title} - {self.rating}'
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Movie Review'
        verbose_name_plural = 'Movie Reviews'



# Create your models here.
