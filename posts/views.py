from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.

def hello_world(request):
    if request.method == "GET":
        return JsonResponse({
            'status': 200,
            'success': True,
            'message': '메시지 전달 성공!',
            'data': 'Hello World!',
        })
    
def introduction(request):
    if request.method == "GET":
        return JsonResponse({
            'status': 200,
            'success': True,
            'message': '메시지 전달 성공!',
            'data': [
                {
                    'name': '정현서',
                    'age': 25,
                    'major': 'Computer Science and Engineering'
                },
                {
                    'name': '홍길동',
                    'age': 23,
                    'major': 'Business Administration'
                }
            ]
        })