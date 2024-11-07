from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import TodoSerializer
from . models import Todos
from rest_framework import status

@api_view(['GET'])
def getTodo(req):
    todo = Todos.objects.all()
    TodoData = TodoSerializer(todo,many=True)
    return Response(TodoData.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def getByIdTodo(req,tid):
    try:
        todo = Todos.objects.get(id=tid)
    except Todos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    TodoData = TodoSerializer(todo,many=False)
    return Response(TodoData.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def addTodo(req):
    todo = TodoSerializer(data=req.data)
    if todo.is_valid():
        todo.save()
        return Response(todo.data,status=status.HTTP_201_CREATED)
    return Response(todo.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateTodo(req,tid):
    try:
        todo = Todos.objects.get(id=tid)
    except Todos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    todoData = TodoSerializer(todo,data=req.data)
    if todoData.is_valid():
        todoData.save()
        return Response(todoData.data)
    return Response(todoData.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteTodo(req,tid):
    try:
        todo = Todos.objects.get(id=tid)
    except Todos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    todo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)