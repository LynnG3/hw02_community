from django.shortcuts import render, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group


def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts сохранить выборку 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
        'text': 'Главная страница',
        'slug_id': 'cats',
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')
    template = 'posts/group_list.html'
    title = f'Записи сообщества {group}'
    context = {
        'title': title,
        'group': group,
        'posts': posts,
        'slug': slug,
    }
    return render(request, template, context)
