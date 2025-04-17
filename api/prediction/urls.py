from django.urls import path, include
from .views import AdultPredictionView, PredictionView
app_name='prediction'

urlpatterns = [
    path('', PredictionView.as_view(), name='hello'), 
    path('predict/', AdultPredictionView.as_view(), name='hello'), 
]
