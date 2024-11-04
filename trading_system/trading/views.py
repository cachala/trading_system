from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieve(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "pk"

class PortfolioValue(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        total_invested = sum(order.total_value() for order in orders)
        return Response({"total_invested": total_invested})
