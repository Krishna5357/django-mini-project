from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

from .serializers import CustomerSerializer
from .models import Customer
import json

@api_view(['GET'])
def api_all_Customers(request):
    api_all_Customers = Customer.objects.all()
    print(api_all_Customers)
    if api_all_Customers:
    	serializer = CustomerSerializer(api_all_Customers, many=True)
    	return Response(serializer.data)
    else:
    	return Response({"Message": 'Customer Not Foud'})


@api_view(['POST'])
def api_add_Customer(request):
    # first_name = request.POST.get("first_name")
    # last_name = request.POST.get("last_name")
    # dob = request.POST.get("dob")
    # gender = request.POST.get("gender")
    # address = request.POST.get("address")
    # email = request.POST.get("email")
    data=json.loads(request.body)
    customer = Customer.objects.create(first_name=data['first_name'],
                                     last_name=data['last_name'],
                                     dob=data['dob'],
                                     gender=data['gender'],
                                     address=data['address'],
                                     email=data['email'])

    return Response({'message': 'customer created'}, status=201)



@api_view(['put'])
def api_put_Customer(request):
    data=json.loads(request.body)
    updaterecord = Customer.objects.filter(first_name = data['first_name']).update(last_name=data['last_name'])
    return Response({'msg':"sucess"},status = 200)


@api_view(['delete'])
def api_delete_Customer(request, first_name):
    first_name=str(first_name)
    try:
        #data=json.loads(request.body)
        Customer = Customer.objects.filter(first_name = first_name)
        Customer.delete()
    except Customer.doesnotexists:
        return Response({'msg':"delete"},status=201)
    return Response({'msg':'no data found'}, status=201)


@api_view(['patch'])
def api_patch_Customer(request):
    data=json.loads(request.body)
    patchrecord = Customer.objects.filter(first_name = data['first_name']).update(last_name=data['last_name'], dob=data['dob'], gender=data['gender'], address=data['address'], email=data['email'])
    return Response({'msg':"update"},status = 200)
