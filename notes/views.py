from django.shortcuts import render

from rest_framework import generics

from rest_framework.response import Response

from rest_framework.views import APIView

from notes.serializers import UserSerializer, TaskSerializer

from notes.models import User, Task

from rest_framework import permissions, authentication

from notes.permissions import OwnerOnly

class UserCreationView(generics.CreateAPIView):

    serializer_class = UserSerializer

    # def post(self,request,*args,**kwargs):

    #     serializer_instance = UserSerializer(data=request.data)

    #     if serializer_instance.is_valid():

    #         data = serializer_instance.validated_data
            
    #         # User.objects.create_user(**data)

    #         # return Response(data=serializer_instance.data)

    #         user_obj = User.objects.create_user(**data)

    #         serializer_instance = UserSerializer(user_obj)

    #         return Response(data=serializer_instance.data)

        
    #     else:

    #         return Response(data=serializer_instance.errors)


class TaskListCreateView(generics.ListCreateAPIView):

    serializer_class = TaskSerializer

    queryset = Task.objects.all()

    # authentication_classes = [authentication.BasicAuthentication]

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    

    # def list(self, request, *args, **kwargs):

    #     qs = Task.objects.filter(owner=request.user)

    #     serializer_instance = TaskSerializer(qs,many=True)

    #     return Response(data=serializer_instance.data)

    def get_queryset(self):

        qs = Task.objects.filter(owner=self.request.user)
       

        if "category" in self.request.query_params:

            category_value = self.request.query_params.get("category")            

            qs = qs.filter(category = category_value)

        if "priority" in self.request.query_params:

            priority_value = self.request.query_params.get("priority")            

            qs = qs.filter(priority = priority_value)

        return qs
    
class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Task.objects.all()

    serializer_class = TaskSerializer

    # authentication_classes = [authentication.BasicAuthentication]

    authentication_classes = [authentication.TokenAuthentication]


    permission_classes = [OwnerOnly]

from django.db.models import Count

class TaskSummaryApiView(APIView):

    # authentication_classes = [authentication.BasicAuthentication]

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request, *args, **kwargs):

        qs = Task.objects.filter(owner=request.user)

        """
        request.user get only if authenication is provided
        """

        category_summary = qs.values("category").annotate(count=Count("category"))

        status_summary = qs.values("status").annotate(count=Count("status"))

        priority_summary = qs.values("priority").annotate(count=Count("priority"))

        task_count = qs.count()

        context = {
            "category_summary" : category_summary,
            "status_summary" : status_summary,
            "priority_summary" : priority_summary,
            "total_count" : task_count

        }

        return Response(data = context)
    
# class TaskCategoryApiView(APIView):

#     authentication_classes = [authentication.BasicAuthentication]

#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, *args, **kwargs):

#         qs = Task.objects.filter(owner = request.user)

#         categories = qs.values_list("category", flat=True).distinct()

#         print(categories)

#         return Response(data=categories)

# only work if user added any task

class CategoryListView(APIView):

    def get(self,request,*args,**kwargs):

        categories = Task.category_choices

        cat = {c for tp in categories for c in tp}

        return Response(data=cat)
