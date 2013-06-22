# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from blog import models

from django.views.decorators.cache import cache_page
import random

def blog(request):
    posts = models.Post.objects.all()
    outstanding_posts = models.Post.objects.all().order_by("-visits")[0:3]
    return render_to_response("public/blog.html",
                              RequestContext(request,
                                             {
                                                 'posts': posts,
                                                 'outstanding_posts': outstanding_posts
                                                 }
                                             )
                              )

@cache_page(60 * 15)
def post(request, post_id):
    post = models.Post.objects.prefetch_related("links").get(id = post_id)
    links = post.links.all()
    post.visits += 1
    post.save()
    outstanding_posts = models.Post.objects.all().order_by("-visits")[0:3]
    return render_to_response("public/post.html",
                              RequestContext(request,
                                             {
                                                 'post': post,
                                                 'links': links,
                                                 'outstanding_posts': outstanding_posts,
                                                 'rand': random.randint(1, 100)
                                                 }
                                             )
                              )
