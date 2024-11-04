from django.urls import path
from . import views

urlpatterns = [
    path("place-order/", views.OrderListCreate.as_view(), name="place-order"),
    path("total-value/", views.PortfolioValue.as_view(), name='total-value'),
    path("<int:pk>/",
        views.OrderRetrieve.as_view(),
        name="individual-data",
    )
]