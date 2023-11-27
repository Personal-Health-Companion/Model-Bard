from django.urls import path
from .views import MyView

urlpatterns = [
    path('detail/', MyView.as_view(), name='my-view'),
    path('detail/<int:id>/', MyView.as_view()),
]