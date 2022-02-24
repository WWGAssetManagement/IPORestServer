from rest_framework.decorators import api_view
from .serializers import DemandForecastSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

@api_view(['GET', 'POST'])
def demand_forecast(request):
    if request.method == 'POST':
        serializer = DemandForecastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        query_dict = request.query_params
        keys=query_dict.get('test')


