from django.shortcuts import redirect, render

from .forms import FeedbackForm


def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_received')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})


def feedback_received(request):
    return render(request, 'feedback_received.html')