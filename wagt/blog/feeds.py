from django.contrib.syndication.views import Feed
from .models import *



class AllPost(Feed):
    title = "Blog de Juan Carlos"
    link = "/rss/"
    description = "Blog personal de Juan Carlos"

    def items(self):
        return BlogPage.objects.all().order_by('-data_pub')[:10]

    def item_title(self, item):
        return item.intro

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return '/rss/'