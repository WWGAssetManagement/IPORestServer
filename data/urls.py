from django.urls import path, include
from .views import (
    DemandForecastDetailView,
    DemandForecastView,
    DemandForecastInProgressView,
    IPOScheduleView,
    IPOScheduleDetailView,
    DCInsideTitleView,
    DCInsideDetailView,
    NaverTrendSearchView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('title', DCInsideTitleView)
router.register('detail', DCInsideDetailView)

demand_router = DefaultRouter()
demand_router.register('forecast', DemandForecastView)

naver_router = DefaultRouter()
demand_router.register('trend', NaverTrendSearchView)

# 참고 사이트: https://berkbach.com/restful-api-in-django-16fc3fb1a238
# 참고 사이트: https://proglish.tistory.com/53
urlpatterns = [
    path('demand/', include(demand_router.urls)),
    path('demand/forecast/detail/<str:name>', DemandForecastDetailView.as_view()),
    path('demand/forecast/inprogress', DemandForecastInProgressView.as_view()),
    path('ipo/shedule', IPOScheduleView.as_view()),
    path('ipo/shedule/detail/<str:name>', IPOScheduleDetailView.as_view()),
    path('dcinside/', include(router.urls)),
    path('naver/', include(naver_router.urls)),
]
