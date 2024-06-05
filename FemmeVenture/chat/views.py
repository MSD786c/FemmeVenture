from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# Create your views here.
from .models import Thread
from django.db.models import Q
from django.db import transaction

@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('-updated')
    context = {
        'Threads': threads
    }
    return render(request, 'messages.html', context)


@login_required
def ChatSearchBar(request):
    search_keyword = request.GET.get('search_keyword', '')

    # Fetch threads associated with the current user
    my_threads = Thread.objects.by_user(user=request.user)

    # Filter threads based on the search keyword and user's participation
    threads = my_threads.filter(
        Q(second_person=request.user, first_person__username__icontains=search_keyword) |
        Q(first_person=request.user, second_person__username__icontains=search_keyword)
    ).prefetch_related('chatmessage_thread').order_by('-updated')

    print(threads)

    context = {
        'Threads': threads,
        'search_keyword': search_keyword,
    }
    return render(request, 'messages.html', context)


@login_required
def thread_allocate(request):
    user_id = request.POST.get('user_id')
    user = request.user

    # Assuming user_id corresponds to the other user involved in the thread
    other_user = get_object_or_404(User, id=user_id)

    # Fetching the thread where the current user is the first person and the other user is the second person
    thread = Thread.objects.filter(first_person=user, second_person=other_user).first()

    if thread:
        thread.Additional_Note = f"{user.username} Threaded {other_user.username} again"
        thread.save()

    # If no thread is found, try fetching the thread where the current user is the second person and the other user is the first person
    if not thread:
        thread = Thread.objects.filter(first_person=other_user, second_person=user).first()
        if thread:
            thread.Additional_Note = f"{user.username} Threaded {other_user.username} again"
            thread.save()

        # If still no thread is found, create a new thread record
        if not thread:
            thread = Thread.objects.create(first_person=user, second_person=other_user)
            thread.Additional_Note = "Create New Thread"
            thread.save()

    return redirect('messages_page')


