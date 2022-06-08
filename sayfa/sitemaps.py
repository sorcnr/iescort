from django.contrib.sitemaps import Sitemap
from sayfa.models import Blog,Eskort

class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.6
    def items(self):
        return Blog.objects.all()

    def location(self, obj: Blog) -> str:
        return obj.get_absolute_url()


class EskortSitemap(Sitemap):
    changefreq = "daily"
    priority = 1

    def items(self):
        return Eskort.objects.all()

    def location(self, obj: Eskort) -> str:
        return obj.get_absolute_url()
