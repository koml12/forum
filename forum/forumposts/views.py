from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
from .models import ForumPost, ForumPostManager, Comment, CommentManager
from .forms import PostForm, CommentForm
from django.views import generic
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from django.views import View

from forumposts.models import ForumPost


# Create your views here.


def hello(request):
    return HttpResponse('Hello! You\'re in the forum')


def fake_add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            link = form.cleaned_data['link']
            post = ForumPost.objects.create_post(text, link)
            post.save()
            return HttpResponse('saved')


def view_posts(request):
    invalid_url = False
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            link = form.cleaned_data['link']
            manager = ForumPostManager()
            post = manager.create_post(text=text, link=link)
            post.save()
        else:
            invalid_url = True

    post_list = ForumPost.objects.order_by().all()
    context = {'post_list': post_list, 'invalid_url': invalid_url}
    return render(request, 'forumposts/main_page.html', context)


def add_post(request):
    return render(request, 'forumposts/add_posts.html', {})


def like_post(request):
    votes = 0
    if request.method == 'GET':
        post_id = request.GET.get('id')
        post = ForumPost.objects.get(id=post_id)
        post.votes = post.votes + 1
        votes = post.votes
        post.save()

    data = {
        'votes': votes
    }
    return JsonResponse(data=data)


def view_comments(request, pk=None):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        print(comment_form.errors)
        if comment_form.is_valid():
            comment_text = comment_form.cleaned_data.get('text')
            manager = CommentManager()
            forumpost = ForumPost.objects.get(id=pk)
            new_comment = manager.add_comment(forumpost, comment_text)
            new_comment.save()
            context = {'forumpost': forumpost}
            return render(request, 'forumposts/forumpost_detail.html', context)
    if request.method == 'GET':
        forumpost = ForumPost.objects.get(id=pk)
        context = {'forumpost': forumpost}
        return render(request, 'forumposts/forumpost_detail.html', context)

