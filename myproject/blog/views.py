from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm

def post_list(request):
	post_list = Post.objects.all().order_by('title')
	paginator = Paginator(post_list, 9)

	page = request.GET.get('page')
	posts = paginator.get_page(page)
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blog/post_detail.html', {'post':post})


@login_required
def post_create(request):
	form = PostForm()

	if request.method == 'POST':

		form = PostForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()

			return redirect('blog:post_list')

	elif request.method == 'GET':
		return render(request, 'blog/add_post.html', {'form':form})


def about(request):
	return render(request, 'blog/about_us.html')

def contact(request):
	return render(request, 'blog/contact.html')