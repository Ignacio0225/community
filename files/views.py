from django.http.multipartparser import MultiPartParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializer import FileSerializer
from .models import File

# Create your views here.

class FileUpload(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self,request):
        pass
