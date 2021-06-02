from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .search_tasks import add_search
import json

# Create your views here.

class AddSearchView(APIView):
    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        body = json.loads(request.body)
        add_search.delay(data=body["words"])
        return Response("Done")
