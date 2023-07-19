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

from django.views.decorators.http import require_http_methods
from .models import Post

@require_http_methods(["GET"])
def get_post_detail(request, id):
    post = get_object_or_404(Post, pk = id)

    category_json = {
        'id': post.post_id,     # Post 모델 객체의 post_id 필드 값 참조
        'writer': post.writer,
        'content': post.content,
        'category': post.category,
    }

    return JsonResponse({
        'status': 200,
        'message': '게시글 조회 성공',
        'data': category_json
    })

@require_http_methods(["GET"])
def get_post_all(request):
    posts = Post.objects.all()

    post_list = list(posts.values())

    return JsonResponse({
        'status': 200,
        'message': '모든 게시글 조회 성공',
        'data': post_list,
    })