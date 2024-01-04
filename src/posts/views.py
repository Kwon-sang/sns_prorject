from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import Post, PostForm


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/post_list.html'

    def get_context_data(self, *args, **kwargs):
        user = self.request.user
        user_tags_all = user.get_tags_all()
        context = super().get_context_data(*args, **kwargs)
        context['user_tags_all'] = user_tags_all
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        username = self.request.GET.get('username')
        tag = self.request.GET.get('tag')
        print(tag)
        if username:
            qs = qs.filter(author__username=username)
            print(qs)
            if tag:
                qs = qs.filter(tags__name__in=[tag])
                print(tag)
            return qs
        return qs


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


@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if post.is_author(request):
        post.photo.delete()
        post.delete()
        messages.success(request, '삭제 되었습니다.')
    else:
        messages.warning(request, '삭제 권한이 없습니다.')
    return redirect('posts:post_list')


@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if post.is_author(request):
        if request.method == 'POST':
            form = PostForm(data=request.POST, instance=post)
            if form.is_valid():
                messages.success(request, '수정 하였습니다.')
                form.save()
        else:
            form = PostForm(instance=post)
            return render(request, 'posts/post_update_form.html', context={'form': form})
    messages.warning(request, '수정 권한이 없습니다.')
    return redirect('posts:post_list')
