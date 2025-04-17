from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class PredictionView(APIView):
    def get(self, request):
        return Response({"message": "PredictionView Phora API"})


class AdultPredictionView(APIView):
    def get(self, request):
        return Response({"message": "AdultPredictionView Phora API"})
