from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .forms import Post, PostForm


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.success(request, "포스팅을 생성하였습니다.")
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'posts/post_create_form.html', {'form': form})


def post_list(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    posts = Post.objects.filter(author=user.id)
    all_tags = []
    for post in posts:
        all_tags += post.tags.all()
    return render(request, 'user/userpage.html', {'posts': posts,
                                                  'username': username,
                                                  'all_tags': all_tags})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post_detail.html', {'post': post})
