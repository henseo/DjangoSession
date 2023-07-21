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
from .models import Post, Comment

'''
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
'''

'''
@require_http_methods(["GET"])
def get_post_all(request):
    posts = Post.objects.all()

    post_list = list(posts.values())

    return JsonResponse({
        'status': 200,
        'message': '모든 게시글 조회 성공',
        'data': post_list,
    })
'''

@require_http_methods(["GET"])
def get_post_all(request):
    # Post DB에 있는 모든 데이터를 불러와서 Queryset 형식으로 저장
    posts = Post.objects.all()

    # 각 데이터를 Json 형식으로 변환하여 리스트에 저장
    post_list = []
    for post in posts:
        post_json = {
            'id': post.post_id,
            'writer': post.writer,
            'category': post.category
        }

        post_list.append(post_json)

    return JsonResponse({
        'status': 200,
        'message': '게시글 목록 조회 성공',
        'data': post_list
    })

def get_comment(request, post_id):
    if request.method == "GET":
        comments = Comment.obejcts.filter(post = post_id)

import json

@require_http_methods(["POST"])
def create_post(request):
    body = json.loads(request.body.decode('utf-8'))

    # ORM을 통해 새로운 데이터를 DB에 생성
    new_post = Post.objects.create(
        writer = body['writer'],
        content = body['content'],
        category = body['category']
    )

    # Response에서 보일 데이터 내용을 Json 형태로 예쁘게 가공
    new_post_json = {
        "id": new_post.post_id,
        "writer": new_post.writer,
        "content": new_post.content,
        "category": new_post.category
    }

    return JsonResponse({
        'status': 200,
        'message': '게시글 목록 조회 성공',
        'data': new_post_json
    })

@require_http_methods(["GET", "PATCH", "DELETE"])
def post_detail(request, id):
    # 요청 메서드가 GET인 경우, 게시글을 조회하는 로직을 처리
    if request.method == "GET":
        post = get_object_or_404(Post, pk = id)  # 주어진 모델에서 특정 객체를 가져오거나 404 오류를 반환

        post_json = {
            "id": post.post_id,
            "writer": post.writer,
            "content": post.content,
            "category": post.category
        }

        return JsonResponse({
            'status': 200,
            'message': '게시글 조회 성공',
            'data': post_json
        })
    
    # 요청 메서드가 PATCH인 경우, 게시글을 수정하는 로직을 처리
    elif request.method == "PATCH":
        body = json.loads(request.body.decode('utf-8'))
        update_post = get_object_or_404(Post, pk = id)

        update_post.content = body['content']
        update_post.save()

        update_post_json = {
            "id": update_post.post_id,
            "writer": update_post.writer,
            "content": update_post.content,
            "category": update_post.category
        }

        return JsonResponse({
            'status': 200,
            'message': '게시글 수정 성공',
            'data': update_post_json
        })
    
    elif request.method == "DELETE":
        delete_post = get_object_or_404(Post, pk = id)
        delete_post.delete()

        return JsonResponse({
            'status': 200,
            'message': '게시글 삭제 성공',
            'data': None
        })
    
@require_http_methods(["GET"])
def get_comment(request, id):
    comments = Comment.objects.filter(post = id)

    comment_json_list = []
    for comment in comments:
        comment_json = {
            "writer": comment.writer,
            "content": comment.content
        }

        comment_json_list.append(comment_json)

    return JsonResponse({
        'status': 200,
        'message': '댓글 읽어오기 성공',
        'data': comment_json_list
    })

@require_http_methods(["POST"])
def create_comment(request, post_id):   # FK: post_id
    body = json.loads(request.body.decode('utf-8'))
    post = get_object_or_404(Post, pk = post_id)

    new_comment = Comment.objects.create(
        writer = body['writer'],
        content = body['content'],
        post = post   # FK
    )

    new_comment_json = {
        "writer": new_comment.writer,
        "content": new_comment.content
    }

    return JsonResponse({
        'status': 200,
        'message': '댓글 생성 성공',
        'data': new_comment_json
    })

import datetime

@require_http_methods(["GET"])
def get_recent_post(request):
    current_session = datetime.datetime(2023, 7, 19, 19, 0)
    next_session = current_session + datetime.timedelta(weeks = 1)

    posts = Post.objects.filter(created_at__gte = current_session, created_at__lt = next_session)

    post_json_list = []
    for post in posts:
        post_json = {
            "id": post.post_id,
            "writer": post.writer,
            "content": post.content,
            "category": post.category,
            "created time": post.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

        post_json_list.append(post_json)

    return JsonResponse({
        'status': 200,
        'message': '세션 이후 일주일 동안 작성된 게시글 조회 성공',
        'data': post_json_list
    })