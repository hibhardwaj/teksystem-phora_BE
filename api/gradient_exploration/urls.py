from django.urls import path, include
from .views import ExplorationView, AdultExplorationView
app_name='gradient'
urlpatterns = [ 
    path('', ExplorationView.as_view(), name='hello'), 
    path('gradient/', AdultExplorationView.as_view(), name='hello')
]
