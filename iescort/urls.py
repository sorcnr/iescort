from django import urls
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from sayfa.views import index_view, escort_view, blog_view
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from sayfa.sitemaps import BlogSitemap,EskortSitemap

sitemaps = {'blogs': BlogSitemap,'escorts':EskortSitemap}


app_name = "iescort"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view,name="main"),
    path('<slug:slug>/',index_view,name="cat_view"),
    path('amp/', index_view,name="amp"),
    path('izmir-escort/<slug:slug>/', escort_view, name="escort_view"),
    path('a/<slug:slug>/',blog_view,name="blog_view"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps,}, name='Sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
