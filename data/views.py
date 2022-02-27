from .serializers import DemandForecastSerializer, IPOScheduleSerializer, DCInsideTitleSerializer
from .models import DemandForecastModel, IPOScheduleModel, DCInsideTitleModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


# Create your views here.
class DemandForecastView(APIView):
    """
    전체 수요예측 일정
    """

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
    """
    종목당 수요예측 일정
    """

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


class DemandForecastInProgressView(APIView):
    def get(self, request):
        datas = DemandForecastModel.objects.filter(ipo_price=None).all()
        serializer = DemandForecastSerializer(datas, many=True)
        return Response(serializer.data)


class IPOScheduleView(APIView):
    def get(self, request):
        datas = IPOScheduleModel.objects.all()
        serializer = IPOScheduleSerializer(datas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IPOScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'name': request.data['name'],
                'response': True
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IPOScheduleDetailView(APIView):
    """
    종목당 IPO 일정
    """

    def get_object(self, name):
        try:
            return IPOScheduleModel.objects.get(name=name)
        except IPOScheduleModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, name):
        data = self.get_object(name)
        serializer = IPOScheduleSerializer(data)
        return Response(serializer.data)

    def put(self, request, name, format=None):
        data = self.get_object(name)
        serializer = IPOScheduleSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DCInsideTitleView(viewsets.ModelViewSet):
    queryset = DCInsideTitleModel.objects.all()
    serializer_class = DCInsideTitleSerializer

    # def create(self, request, *args, **kwargs):
    # Row 하나씩 업데이트
    #     data = request.data
    #     serializer = self.get_serializer(data=data)
    #     if serializer.is_valid():
    #         headers = self.get_success_headers(data=data)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        # 한꺼번에 Insert
        data = request.data
        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid()
        self.perform_create(serializer)
        headers = self.get_success_headers(data=data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
