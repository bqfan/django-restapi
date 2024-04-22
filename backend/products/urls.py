from django.urls import path
from . import views


urlpatterns = [
    path("", views.product_all_view),
    path("<int:pk>/", views.product_all_view),
]
