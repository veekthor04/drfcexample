from django.urls import include, path
from .views import CarView

urlpatterns = [
    path('car/', CarView.as_view(), name='carview'),
]