from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import generics
import jwt
import re
from rest_framework.permissions import IsAuthenticated,IsAdminUser , IsAuthenticatedOrReadOnly
from django.contrib.auth.hashers import check_password
import datetime
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.

def verifyToken(token):
       
     try:   
           payload = jwt.decode(
              jwt=token, key='secret-1223', algorithm=['HS256']
           )
           emp = AccessToken.objects.filter(emp_id=payload.get('id')).first()

           if emp is None:
              raise AuthenticationFailed("Token is invalid or deleted")
            


     except (jwt.InvalidSignatureError,jwt.InvalidTokenError) :
            raise AuthenticationFailed('Unauthenticated!')
     

def getToken( request):
        
        header = request.headers.get('Authorization')
        if  header is None :  
          raise AuthenticationFailed("No token is provided")
        if header is not None:
          if "Bearer" in header:
           token = header.split(' ')[1]
           return token
        raise AuthenticationFailed("Invalid Token Type must be Bearer")
 

@api_view(['GET','POST'])
@permission_classes([IsAdminUser])
def getEmployees(request):

   if request.method == "GET":
        employees = Employee.objects.all()
        serializer = EmployeesSerializer(employees, many=True)
        return Response({
            'message': 'success',
            'data': serializer.data
        }, status=200)
   
   elif  request.method == "POST":
       
        serializer = EmployeesPostSerializer(data=request.data)
        if serializer.is_valid() :
           
         serializer.save()
         return Response({
          
         serializer.data
        }, status=200)
        return Response(serializer.errors,status=200)


@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAdminUser])
def getEmployeeDetail(request,pk) :
    try:
        employee = Employee.objects.get(pk=pk)
        serializers = EmployeesSerializer(employee)
    except Employee.DoesNotExist:
        return Response({
            'message': "Employee not found"
        }, status=status.HTTP_404_NOT_FOUND)


    if request.method == "GET":
     try:
        return Response(serializers.data,status= status.HTTP_200_OK)
     except Employee.DoesNotExist:
        return Response({
            'message': "Employee not found"
        }, status=status.HTTP_404_NOT_FOUND)
     
    if request.method == "PUT":
 
        serializer = EmployeesPostSerializer(employee, data=request.data)
        if serializer.is_valid():
         serializer.save()  
         return Response(serializer.data,status= status.HTTP_200_OK)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

     
    if request.method == "DELETE":
       employee.delete()
       return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
     

class ActivityEmpList(APIView):


    def get(self,request):
     token =  getToken(request=request) 
     if token is None :
        raise AuthenticationFailed("No token is provide")
     verifyToken(token)
     activity = ActivityEmployee.objects.all()
     serializers =  ActivityEmpSerializer(activity, many=True)
     return Response(serializers.data,status=status.HTTP_200_OK)

     
    def post(self,request):
     serializers = ActivityPostEmpSerializer(data=request.data)
     if serializers.is_valid(): 
       serializers.save()
       return Response(serializers.data,status=status.HTTP_201_CREATED)
     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

     
    def put(self,request,*args, **kwargs):
     pass
    def delete(self,request,*args, **kwargs):
     pass

class ActivityEmpDetail(APIView):
    def get_object(self,pk):
     try:
      return ActivityEmployee.objects.get(pk=pk)
     except ActivityEmployee.DoesNotExist:
        
      return Response({
        'message':f"no acvitity found with the {pk}"
     },status=status.HTTP_204_NO_CONTENT) 
    def get(self,request,pk):
     print(pk)
    #  return Response({'message':f"hello {pk}"})

     if pk is not None:
     
        
        emp = self.get_object(pk)
        print(emp)
        
        serializer = ActivityEmpSerializer(emp)

    
        return Response(status=status.HTTP_200_OK)
 
     pass
    def post(self,request):
     pass
    def put(self,request,*args, **kwargs):
     pass
    def delete(self,request,*args, **kwargs):
     pass


@api_view(["GET"])
def ActivityEmpOutlet(request,id):
  
  if request.method == "GET":

    try:
     emp = Employee.objects.get(pk=id)
     try:
       result = ActivityEmployee.objects.filter(emp_id = emp.pk)

       if result.exists() :
         serializers = ActivityEmpSerializer(result,many=True)
         return Response(serializers.data,status=status.HTTP_204_NO_CONTENT)

     except ActivityEmployee.DoesNotExist:
       return Response(status=status.HTTP_204_NO_CONTENT)

    except Employee.DoesNotExist:
      return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(["POST"])
def ActivityDateDetailOutlet(request):

  if request.method == "POST":
   serializers = ActivityEmpDateSerializer(data=request.data)

   if serializers.is_valid(): 
     emp_id = serializers.validated_data.get("emp_id")
     date = serializers.validated_data.get("date")
     result = ActivityEmployee.objects.filter(emp_id=emp_id,date=date)
     serializersActivity = ActivityEmpSerializer(result,many=True)
     print(emp_id,date)
     return Response(serializersActivity.data,status=status.HTTP_200_OK)
   return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
#   result = ActivityEmployee.objects.
   

class CompanyOutletListCreate(generics.ListCreateAPIView):
    permission_classes =[IsAuthenticatedOrReadOnly]
    queryset = CompanyOutlet.objects.all()
    serializer_class = CompanyOutletSerializer

class CompanyOutletDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes =[IsAuthenticatedOrReadOnly]
    queryset = CompanyOutlet.objects.all()
    serializer_class = CompanyOutletSerializer


        

@api_view(["POST"])
def empLogin(request):
    serializers = EmployeesLoginSerializer(data=request.data)
    if serializers.is_valid():
        email = request.data.get('email')

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return Response({'message': 'Invalid email format'}, status=status.HTTP_400_BAD_REQUEST)

        emp = Employee.objects.filter(email=email).first()
        if emp is None:
            return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # Hash the provided password before checking it
  
        password = serializers.validated_data.get('password')
        payload = {
            'id': emp.id,
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.now()
        }

        token = jwt.encode( payload,'secret-1223',algorithm='HS256').decode('utf-8')
        AccessToken.objects.create(emp_id=emp, token=token)
        response = Response()
        response.set_cookie(
          key='jwt',
          value=token,
          expires=datetime.datetime.now() + datetime.timedelta(minutes=60),
           httponly=True
        )
        response.data = {'message': 'Login successful','token':token}
        if check_password(password, emp.password):
            # Call JWT payload here 
            return response
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def empRegister(request):
 if request.method == "POST":
  
  serializers = EmployeesCreateSerializer(data=request.data)
 
  if serializers.is_valid():
   isExist = Employee.objects.filter(email = serializers.validated_data.get('email')).first()
   if isExist is not None :

     return Response({'message':'email is already register'},status=status.HTTP_202_ACCEPTED)
   serializers.save()


   return Response({
     'message':'successfully register please wait for admin to comfirm'
   },status=status.HTTP_201_CREATED)
 return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
  


@api_view(["POST"])

def empLogout(request):
    response = Response()
    response.delete_cookie('jwt')
    token = getToken(request)
    accessToken = AccessToken.objects.filter(token=token).first()
    if accessToken is not None:
     accessToken.delete()
     response.data = {'message':" logout successfully"}
     return response
    raise AuthenticationFailed("Invalid Token")
    
