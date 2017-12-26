# Create your views here.
#coding=utf-8
from django.shortcuts import render
from blog.models import BlogsPost
from django.shortcuts import render_to_response

def index(request):
	blog_list=BlogsPost.objects.all()
	return render_to_response('index.html',{'blog_list':blog_list})
