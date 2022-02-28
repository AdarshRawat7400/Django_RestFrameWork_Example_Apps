from django.urls import include, path
from .routers import router

urlpatterns = [
    path('viewset/',include(router.urls),name='viewset1'),
    path('viewset/<int:pk>/',include(router.urls),name='viewset1'),

]

# urlpatterns += router2.urls