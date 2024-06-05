from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post, Reply
from .forms import PostForm

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post, Reply
from .forms import PostForm

from .forms import PostForm
from django.contrib import messages

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, 'Post created successfully!')
            return render(request, 'forum/post_create.html', {'form': form})  # Assuming you have a URL named 'forum'
    else:
        form = PostForm()
    return render(request, 'forum/post_create.html', {'form': form})

def forum(request):
    posts = Post.objects.all()
    return render(request, 'forum/forum.html', {'posts': posts})

def like_post(request):
    if request.method == 'POST' and request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        post.likes_count += 1
        post.save()
        return JsonResponse({'likes_count': post.likes_count}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
    
def submit_reply(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        reply_content = request.POST.get('reply_content')
        
        post = Post.objects.get(pk=post_id)
        reply = Reply.objects.create(post=post, content=reply_content)
        
        # You can add additional logic here, such as redirecting the user
        # to the post detail page after submitting the reply
        return redirect('post_detail', pk=post_id)