from django.shortcuts import render

posts = [
    {
        'author': 'Edgaras',
        'title': 'Blog post 1',
        'content': 'First post',
        'date': '2020 liep 29'
    },
    {
        'author': 'Sarune',
        'title': 'Blog post 2',
        'content': 'Second post',
        'date': '2020 liep 29'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html/', context)


def bybis(request):
    return render(request, 'blog/about.html/', {'title': 'about'})
# Create your views here.
