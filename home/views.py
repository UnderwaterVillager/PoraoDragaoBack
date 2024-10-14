# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import viewsets
from home.serializers import UserSerializer
from home.models import User
