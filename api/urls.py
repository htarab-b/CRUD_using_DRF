from django.urls import path
from .views import *

urlpatterns = [
    path('', NameListView.as_view()),
]
