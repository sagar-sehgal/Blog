from django.shortcuts import redirect,render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.utils import timezone

# Create your views here.
def post_list(request):
	all_posts=Post.objects.all().order_by("created_date")
	return render(request,"blog/post_list.html",{'all_posts':all_posts})
def post_detail(request,id):
	obj=get_object_or_404(Post,pk=id)
	return render(request,"blog/post.html",{'post':obj})
def post_new(request):
	if(request.method=="POST"):
		form=PostForm(request.POST)
		if(form.is_valid()):
			post=form.save(commit=False)
			post.author=request.user
			post.published_date=timezone.now()
			post.save()
			return redirect("post_detail",id=post.id)
	else:
		form=PostForm()
	return render(request,'blog/post_edit.html',{'form':form})
def post_edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if(request.method== "POST"):
        form = PostForm(request.POST, instance=post)
        if(form.is_valid()):
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail.html', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
