
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Board
from rest_framework import generics, viewsets, status
from api.serializers import BoardSerializer , UserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied
from .permissions import IsOwnerOrReadOnly




class Gamelist(generics.ListAPIView):
    """
    API endpoint that allows users to list all the GameBoard .
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer



class CreateBoardView(APIView):
    """
    API endpoint that allows users to create the GameBoard .
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        agame = Board.objects.create(created_by = request.user)
        agame.save()
        return Response(BoardSerializer(agame).data, status = status.HTTP_201_CREATED)
    



class getBoard(APIView):
    """
    API endpoint that allows users to view the GameBoard .
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        game = Board.objects.get(id = pk)
        game  = BoardSerializer(game)
        return Response(game.data, status = status.HTTP_200_OK)


class updateBoard(generics.UpdateAPIView):
    """
    API endpoint that allows users to update GameBoard to edited.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [ IsOwnerOrReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication]





# class testing(APIView):
#     def get(self, request):
#         # print(request.user)
#         data = Board.objects.first()
#         data = BoardSerializer(data).data        
#         some = {'some': 'some'}        
#         return Response(some)