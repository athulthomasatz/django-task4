
from django.urls import path,include
from myapp.views import hello,thomman

urlpatterns = [
    path('hello/',hello),
    path('athul/',thomman)
]  