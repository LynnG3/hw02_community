from django.shortcuts import render, get_object_or_404
from .models import Post, Group

NUM_ENTRIES: int = 10


def index(request):
    posts = Post.objects.all().select_related('group')[:NUM_ENTRIES]
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    # функция для страниц с записями групп
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.all().select_related('group')[:NUM_ENTRIES]
    template = 'posts/group_list.html'
    title = f'Записи сообщества {group}'
    context = {
        'title': title,
        'group': group,
        'posts': posts,
        'slug': slug,
    }
    return render(request, template, context)
