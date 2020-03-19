from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')


def about_weather1(request):
    return render(request, 'blog/about_weather1.html')


def about_weather2(request):
    return render(request, 'blog/about_weather2.html')


def about_weather3(request):
    return render(request, 'blog/about_weather3.html')
