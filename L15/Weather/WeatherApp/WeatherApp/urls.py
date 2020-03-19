
from django.contrib import admin
from django.urls import path, include

urlpatterns = {
    path('admin/', admin.site.urls),
    path('', include('weather.urls')),
    path('home/', include('weather.urls')),
    path('blog/', include('blog.urls')),
    path('blog/about_weather1', include('blog.urls')),
    path('blog/about_weather2', include('blog.urls')),
    path('blog/about_weather3', include('blog.urls')),
}
