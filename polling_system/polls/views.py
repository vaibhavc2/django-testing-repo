from django.shortcuts import render

from .forms import VoteForm
from .models import Poll


def poll_detail(request, pk):
    poll = Poll.objects.get(pk=pk)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.poll = poll
            vote.user = request.user
            vote.save()
    else:
        form = VoteForm()
    return render(request, 'poll_detail.html', {'poll': poll, 'form': form})