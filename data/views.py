from .serializers import DemandForecastSerializer
from .models import DemandForecastModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class DemandForecastView(APIView):
    def get(self, request):
        datas = DemandForecastModel.objects.all()
        serializer = DemandForecastSerializer(datas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DemandForecastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'name': request.data['name'],
                'response': True
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DemandForecastDetailView(APIView):
    def get_object(self, name):
        try:
            return DemandForecastModel.objects.get(name=name)
        except DemandForecastModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, name):
        data = self.get_object(name)
        serializer = DemandForecastSerializer(data)
        return Response(serializer.data)

    def put(self, request, name, format=None):
        data = self.get_object(name)
        serializer = DemandForecastSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
