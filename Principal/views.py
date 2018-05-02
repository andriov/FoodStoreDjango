# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product
from django.http import JsonResponse

# Create your views here.
class ProductList(generics.ListCreateAPIView):
	queryset=Product.objects.all()
	serializer_class=ProductSerializer
