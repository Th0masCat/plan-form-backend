from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlanInfoSerializer
from .models import Plan

# Create your views here.

class PlanView(viewsets.ModelViewSet):
    serializer_class = PlanInfoSerializer
    queryset = Plan.objects.all()
