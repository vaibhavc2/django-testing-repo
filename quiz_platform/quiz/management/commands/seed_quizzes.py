from django.core.management.base import BaseCommand
from quiz.models import Answer, Question, Quiz


class Command(BaseCommand):
    help = 'Seeds the database with quizzes'

    def handle(self, *args, **options):
        # Create quizzes, questions, and answers
        # For example:
        quiz = Quiz.objects.create(title='Quiz 1', description='A sample quiz')
        question = Question.objects.create(quiz=quiz, text='What is 2 + 2?')
        Answer.objects.create(question=question, text='4', is_correct=True)
        Answer.objects.create(question=question, text='5', is_correct=False)