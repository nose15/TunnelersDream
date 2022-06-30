from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('<str:x>^<str:z>^<str:x_margin>^<str:z_margin>^<str:x1>^<str:z1>^<str:x_margin1>^<str:z_margin1>/', views.tunnel, name="tunnel"),
    path('credits/', views.credits, name="credits")
]