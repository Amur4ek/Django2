from django.urls import path
from demo11.views import ingredients

urlpatterns = [
    path('<str:dish>/', ingredients),
]


###