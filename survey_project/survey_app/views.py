from django.shortcuts import redirect, render

from .forms import QuestionForm, SurveyForm


def create_survey(request):
  if request.method == 'POST':
    form = SurveyForm(request.POST)
    if form.is_valid():
      survey = form.save()
      # Handle questions here
      return redirect('success')
  else:
    form = SurveyForm()
  return render(request, 'create_survey.html', {'form': form})


def success(request):
    return render(request, 'success.html')