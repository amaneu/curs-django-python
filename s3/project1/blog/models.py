# -*- coding: utf-8 -*-
from django.db import models
from django.utils.timezone import utc
import datetime
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse

class Post(models.Model):
    # Relations
    
    # Attributes
    title = models.CharField(max_length = 300,
                             verbose_name = u"title")
    short_body = models.TextField(verbose_name = u"short body")
    body = models.TextField(verbose_name = u"body")
    created_at = models.DateTimeField(verbose_name = u"created at")
    published_at = models.DateTimeField(verbose_name = u"published at")
    visits = models.IntegerField(default = 0,
                                 verbose_name = u"visits")
    
    # Functions
    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ("post", [str(self.id)])

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.utcnow().replace(tzinfo = utc)
        super(Post, self).save(args, kwargs)

    class Meta:
        ordering = ["-published_at"] 

class Link(models.Model):
    # Relations
    post = models.ForeignKey(u"Post",
                             related_name = u"links",
                             verbose_name = u"post")
    
    # Attributes
    uri = models.URLField(verbose_name = u"URI")
    name = models.CharField(max_length = 200,
                            verbose_name = u"name")
    # Functions
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class BlogStats(models.Model):
    num_requests = models.IntegerField(default = 0)

    class Meta:
        pass

class LatestEntriesFeed(Feed):
    title = u"Feed de posts del blog"
    link = u"/blabal"
    description = u"Això és un exemple de feed RSS de posts del blog"

    def items(self):
        return Post.objects.order_by('-published_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.short_body

    def item_link(self, item):
        return reverse('post', args=[item.id])