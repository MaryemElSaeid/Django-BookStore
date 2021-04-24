from rest_framework.response import Response 
from rest_framework import status 
from booklets.models import Booklet
from .serializers import BookletSerializer , UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def index(request):
    booklets=Booklet.objects.all()
    serializer=BookletSerializer(instance=booklets,many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)


@api_view(["POST"])
def create(request):
    serializer=BookletSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success":True,
            "message":"Booklet has been created"
        },status=status.HTTP_201_CREATED)
    return Response(data={
        "success":False,
        "errors":serializer.errors
    },status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def edit(request,id):
    booklets = Booklet.objects.get(pk=id)
    serializer=BookletSerializer(instance=booklets,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success":True,
            "message":"Booklet has been updated"
        },status=status.HTTP_200_OK)
    return Response(data={
        "success":False,
        "errors":serializer.errors
    },status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def show(request,id):
    booklets=Booklet.objects.get(pk=id)
    serializer=BookletSerializer(instance=booklets,many=False)
    return Response(data=serializer.data,status=status.HTTP_200_OK)
        

@api_view(["DELETE"])
def delete(request,id):
    booklet = Booklet.objects.get(id=id)
    booklet.delete()
    return Response ('Deleted')


@api_view(["POST"])
def api_signup(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success":True,
            "message":"User has been registered"
        },status=status.HTTP_200_OK)
    return Response(data={
        "success":False,
        "errors":serializer.errors
    },status=status.HTTP_400_BAD_REQUEST)



