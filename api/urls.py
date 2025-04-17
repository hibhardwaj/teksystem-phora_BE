from django.urls import path, include
from django.views.generic import RedirectView
app_name='api'
urlpatterns = [
    path('', RedirectView.as_view(url='prediction/', permanent=False)),
    path('prediction/', include('api.prediction.urls')),
    path('exploration/', include('api.gradient_exploration.urls')), 
]
