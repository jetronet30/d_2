from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    Http404,
    HttpResponseRedirect,
    HttpResponsePermanentRedirect,
)
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

from women.models import Women, Category, TagPost

def add_in_db(title, content):
    obj, created = Women.objects.get_or_create(
        title=title,
        defaults={'content': content}
    )
    #Women.objects.filter(title=title).exists()
 
    return obj, created

menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},
]

data_db = [
    {
        "id": 1,
        "title": "Анджелина Джоли",
        "content": """<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
    Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».""",
        "is_published": True,
    },
    {
        "id": 2,
        "title": "Марго Робби",
        "content": "Биография Марго Робби",
        "is_published": False,
    },
    {
        "id": 3,
        "title": "Джулия Робертс",
        "content": "Биография Джулия Робертс",
        "is_published": True,
    },
]

cats_db = [
    {
        "id": 1,
        "name": "Актрисы",
        "slug": "aktrisy",
    },
    {
        "id": 2,
        "name": "Сценаристы",
        "slug": "scenaristy",
    },
    {
        "id": 3,
        "name": "Режиссёры",
        "slug": "rezhissery",
    },
]



def index(request):
    # add_in_db("Orlado Bloom", "Orlado Bloom")
    # for w in Women.objects.all():
    #     w.slug = 'slug-' + str(w.id)
    #     w.save()
    posts = Women.published.all()
    data = {
        "title": "Главная страница",
        "menu": menu,
        "posts": posts,
        "cat_selected": 0,
    }
    cats = Category.objects.all()
    name = Women.objects.filter(cat_id__in=cats)
    c = Category.objects.get(pk=1)
    
    print(name, c.posts.filter(is_published=1))

    print('########################################')

    print(Women.objects.filter(cat__slug='aktrisy'))


    print('########################################')

    a = Women.objects.get(pk=1)
    tag_br = TagPost.objects.all()
    print(tag_br)

    tag_o, tag_v =TagPost.objects.filter(id__in=[3, 5])

    a.tags.set([tag_o, tag_v, tag_br[0]])

    a.tags.remove(tag_o)

    a.tags.add(tag_br[0])
    return render(request, "women/index.html", context=data)


def about(request):
    return render(request, "women/about.html", {"title": "О сайте", "menu": menu})


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    data = {
        "title": post.title,    
        "menu": menu,
        "post": post,
        "cat_selected": 1
    }
    return render(request, "women/post.html", context=data)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk)
    data = {
        "title": f"Категория {category.name} ",
        "menu": menu,
        "posts": posts,
        "cat_selected": category.pk,
    }
    return render(request, "women/index.html", context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
