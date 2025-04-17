from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class ExplorationView(APIView):
    def get(self, request):
        return Response({"message": "ExplorationView Phora API"})


class AdultExplorationView(APIView):
    def get(self, request):
        return Response({"message": "AdultExplorationView Phora API"})
