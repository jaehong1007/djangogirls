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
