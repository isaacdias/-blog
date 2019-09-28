from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm
from .forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage



def post_list(request):
    post_list = Post.objects.all().order_by('title')
    paginator = Paginator(post_list, 9)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_create(request):
    form = PostForm()

    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('blog:post_list')

        else:
            return render(request, 'blog/add_post.html', {'form': form})

    elif request.method == 'GET':
        return render(request, 'blog/add_post.html', {'form': form})


@login_required
def post_update(request, id):
    post = get_object_or_404(Post, pk=id)
    form = PostForm(instance=post)

    if(request.method == 'POST'):
        form = PostForm(request.POST, request.FILES, instance=post)

        if(form.is_valid()):

            post.save()

            return redirect('blog:post_list')
        else:
            return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

    elif(request.method == 'GET'):
        return render(request, 'blog/edit_post.html', {'form': form, 'post': post})


@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('blog:post_list')


def about(request):
    return render(request, 'blog/about_us.html')


def contact(request):
        Contact_Form = ContactForm
        if request.method == 'POST':
            form = Contact_Form(data=request.POST)

            if form.is_valid():
                name = request.POST.get('name')
                email = request.POST.get('email')
                message = request.POST.get('message')

                template = get_template('blog/contact_form.txt')
                context = {
                    'name': name,
                    'email': email,
                    'message': message,
                }

                content = template.render(context)

                email = EmailMessage(
                    "New contact form email",
                    content,
                    "Blog Blocos de Olinda " + '',
                    ['blogdjangoframework@gmail.com'],
                headers={'Reply To': email}
                )

                email.send()

                return render(request, 'blog/contact.html', {'form': Contact_Form})
        return render(request, 'blog/contact.html', {'form':Contact_Form })
