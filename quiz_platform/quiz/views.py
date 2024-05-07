# Create your views here.
from django.shortcuts import redirect, render

from .models import Answer, Question, Quiz


def quiz_list(request):
    quiz_list = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quiz_list': quiz_list})

def quiz_detail(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz})


def submit_answer(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    if request.method == 'POST':
        score = 0
        for question in quiz.question_set.all():
            selected_answer_id = request.POST.get(f'question_{question.id}')
            if selected_answer_id:
                answer = Answer.objects.get(pk=selected_answer_id)
                if answer.is_correct:
                    score += 1
        # Save the score to the session or the database
        request.session['score'] = score
        return redirect('quiz_results', pk=quiz.id)
    else:
        return redirect('quiz_detail', pk=quiz.id)


def quiz_results(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    score = request.session.get('score', 0)
    return render(request, 'quiz/quiz_results.html', {'quiz': quiz, 'score': score})