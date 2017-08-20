from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.
def post_list(request):
	all_posts=Post.objects.all().order_by("created_date")
	return render(request,"blog/post_list.html",{'all_posts':all_posts})
def post_detail(request,id):
	obj=get_object_or_404(Post,pk=id)
	return render(request,"blog/post.html",{'post':obj})