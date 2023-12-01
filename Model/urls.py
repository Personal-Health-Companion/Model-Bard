from django.urls import path
from .views import MyView

urlpatterns = [
    path('bard/<int:id>/', MyView.as_view()),
]