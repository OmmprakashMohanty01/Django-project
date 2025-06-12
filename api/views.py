from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
def public_view(request):
    return Response({"message": "✅ This is a public endpoint. No authentication required."})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": f"🔐 Hello, {request.user.username}. This is a protected endpoint."})
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import test_task

@api_view(['GET'])
def run_test_task(request):
    test_task.delay()  # run task asynchronously
    return Response({"message": "✅ Task triggered!"})
