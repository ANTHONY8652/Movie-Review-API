"""
URL configuration for Movie_Review_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title = 'Movie Review API',
        default_version = 'v1.0.0',
        description = 'The Movie Review API allows users to create, read, update, and delete (CRUD) movie reviews. Built with Django and Django REST Framework (DRF), this API enables interaction with a database of user-generated movie reviews.',
        terms_of_service = 'https://google.com/policies/terms',
        contact = openapi.Contact(email='githinjianthony720@gmail.com'),
        license = openapi.License(name='MIT License'),
    ),
    public = True,
    permission_classes = [permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-with-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-with-ui'),
    path('api/users/', include('users.urls'), name='users'),
    path('api/', include('reviews.urls'), name='reviews'),
]
