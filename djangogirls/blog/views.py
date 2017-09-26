from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def post_list(request):
    # post_list view가 published_date가 존재하는 Post목록만 보여주도록 수정

    posts = Post.objects.filter(published_date__isnull=False)
    context = {
        # posts key의 value는 QuerySet
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


# post_detail 기능을 하는 함수를 구현
# 'post'라는 key로 Post.objects.first()에 해당하는 Post 객체를 전달
# 템플릿은 'blog/post_detail.html'을 사용

# 실제 템플릿파일 생성
# 'post'라는 변수를 이용하 Post객체의 내용을 출력

def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse('No Post', status=404)

    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)



