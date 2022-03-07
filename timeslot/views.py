from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializers
from .models import Register
from datetime import datetime


# Create your views here.


@api_view(['GET'])
def RegisterList(request):
    datas = Register.objects.all()
    serializer = RegisterSerializers(datas, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def User_Register(request):
    serializer = RegisterSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def TimeSlots(request, inter_id, cand_id):
    data1 = Register.objects.get(id=inter_id)
    data2 = Register.objects.get(id=cand_id)
    serializer1 = RegisterSerializers(data1, many=False)
    serializer2 = RegisterSerializers(data2, many=False)
    date1 = datetime.strptime(serializer1.data['time_from'], '%H:%M:%S').time()
    date2 = datetime.strptime(serializer1.data['time_to'], '%H:%M:%S').time()
    date3 = datetime.strptime(serializer2.data['time_from'], '%H:%M:%S').time()
    date4 = datetime.strptime(serializer2.data['time_to'], '%H:%M:%S').time()
    list1 = []
    for i in range(max(date1, date3).hour, min(date2, date4).hour):
        list1.append((i, i + 1))

    if not list1:
        return Response("you don't have slots for this candidate")
    else:
        return Response(list1)
