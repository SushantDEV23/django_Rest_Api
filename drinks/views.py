from django.http import JsonResponse
from requests import Response
from .models import Drink
from .serializers import DrinkSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])              #We have used a decorator here
def drink_list(request, format=None):

    if(request.method=='GET'):     
        #get all the drinks
        #serialize them
        #return json
        drinks=Drink.objects.all()
        serializer=DrinkSerializers(drinks, many=True)
        return Response(serializer.data)  #in Json format, data here will return dictionary and safe means we can convert non-dict elements to Json format
    #return JsonResponse({'drinks':serializers.data}, safe=False)   #in Object 

    if(request.method=='POST'):
        serializer=DrinkSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_details(request, id, format=None):

    try:
        drink=Drink.objects.get(pk=id)                #Assigning the value of id to pk(primary key)

    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if(request.method=='GET'):
        serializer=DrinkSerializers(drink)
        return Response(serializer.data)               #we use Response so that it shows the output in HTML with Json format

    elif(request.method=='PUT'):
        serializer=DrinkSerializers(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='DELETE'):
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
        