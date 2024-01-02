from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

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


def post_list(request):
    pass

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post_detail.html', {'post': post})


