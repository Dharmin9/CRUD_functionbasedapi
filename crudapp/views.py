from rest_framework import status
from rest_framework.decorators import api_view
from .models import Students
from .serializers import StudentsSerializer
from rest_framework.response import Response


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def student_api(request, pk=None):
    if request.method == "GET":
        id = pk
        if id is not None:
            get_data = Students.objects.get(id=id)
            serializer = StudentsSerializer(get_data)
            return Response(serializer.data)
        get_data = Students.objects.all()
        serializer = StudentsSerializer(get_data, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serialzer = StudentsSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response({"msg": "data created"}, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PUT":
        id = pk
        get_data = Students.objects.get(pk=id)
        serializer = StudentsSerializer(get_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "full data updated successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
        id = pk
        get_data = Students.objects.get(pk=id)
        serializer = StudentsSerializer(get_data, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Partial updated successfully"})
        return Response(serializer.errors)

    if request.method == "DELETE":
        id = pk
        get_data = Students.objects.get(pk=id)
        get_data.delete()
        return Response({"msg": "data are delted"})
