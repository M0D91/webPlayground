from django.urls import path

# Formato de redireccionado del modelo basado en funciones FBV
# from . import views

# urlpatterns = [
#     path('', views.home, name="home"),
#     path('sample/', views.sample, name="sample"),
# ]

# Formato de redireccionado del modelo basado en clases CBV
from .views import HomePageView, SamplePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('sample', SamplePageView.as_view(), name='sample'),
]