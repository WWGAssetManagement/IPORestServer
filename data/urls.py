from django.urls import path, include
from .views import (
    DemandForecastDetailView,
    DemandForecastView,
    DemandForecastInProgressView,
    IPOScheduleView,
    IPOScheduleDetailView,
)

# 참고 사이트: https://berkbach.com/restful-api-in-django-16fc3fb1a238
# 참고 사이트: https://proglish.tistory.com/53
urlpatterns = [
    path('demand/forecast', DemandForecastView.as_view()),
    path('demand/forecast/detail/<str:name>', DemandForecastDetailView.as_view()),
    path('demand/forecast/inprogress', DemandForecastInProgressView.as_view()),
    path('ipo/shedule', IPOScheduleView.as_view()),
    path('ipo/shedule/detail/<str:name>', IPOScheduleDetailView.as_view()),
]
