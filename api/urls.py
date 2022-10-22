
from django.contrib import admin
from django.urls import include, path
from .views import  Gamelist, CreateBoardView, UserViewSet,  updateBoard, getBoard
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('createboard/', CreateBoardView.as_view(),  ),
    path('gamelist/', Gamelist.as_view(),  ),
    path('getBoard/<int:pk>/', getBoard.as_view(),  ),
    path('updateBoard/<int:pk>/', updateBoard.as_view(),  ),
    # path('testing/', testing.as_view(),  ),


 ]


urlpatterns += [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]