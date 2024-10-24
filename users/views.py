from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate
from .serializers import UserSerializer, UserLoginSerializer, UserLogoutSerializer
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

User = get_user_model()


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(email=email).exists():
            return Response({'detail': 'User with this email already exists try using another email.'})
        
        user =User(
            username = username,
            email = email,
            password = make_password(password)
        )
        user.save()

        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'user': UserSerializer(user).data,
            'token': token.key,
            'redirect_url': 'http://localhost:8000/api/login/'
        }, status=status.HTTP_201_CREATED)
    
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({
                'User': UserSerializer(user).data,
                'token': token.key,
                'redirect_url': 'http://localhost:8000/api/reviews'
            }, status=status.HTTP_202_ACCEPTED)
        
        return Response({'detail': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutView(generics.GenericAPIView):
    serializer_class = UserLogoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            token = request.auth
            token.delete()

            return Response({
                'message': "Successfully Loggged out sad to see you go.",
                'redirect_url': 'http://localhost:8000/api/login/',
            }, status=status.HTTP_204_NO_CONTENT)
        
        except (AttributeError, Token.DoesNotExist):
            return Response({'detail': 'Token not found or already logged out, Try again.'})
        

        
# Create your views here.
