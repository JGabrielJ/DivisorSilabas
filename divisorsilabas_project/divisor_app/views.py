from django.conf import settings
from .analyzer import WordAnalyzer
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import WordForm, FeedbackForm


def main_view(request):
    word_form = WordForm()
    feedback_form = FeedbackForm()
    context = {
        'result': None,
        'word_form': word_form,
        'error_messages': None,
        'feedback_success': None,
        'feedback_form': feedback_form,
    }

    if request.method == 'POST':
        if 'submit_word' in request.POST:
            word_form = WordForm(request.POST)
            if word_form.is_valid():
                a = WordAnalyzer(word_form.cleaned_data['word'])
                context['result'] = {
                    'word': a.word,
                    'syl_word': a.get_syllables(),
                    'num_letters': a.count_letters(),
                    'num_syllables': a.count_syllables()
                }
            else:
                if 'word' in word_form.errors:
                    context['error_messages'] = word_form.errors['word']

        elif 'submit_feedback' in request.POST:
            feedback_form = FeedbackForm(request.POST)
            if feedback_form.is_valid():
                feedback_text = feedback_form.cleaned_data['feedback']
                send_mail (
                    subject='Feedback - Divisor de Sílabas',
                    message=feedback_text,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['jgabrielj.games77@gmail.com'],
                    fail_silently=False,
                ); context['feedback_success'] = "Obrigado pelo seu feedback!"
                # Consertar o problema de reenvio de e-mail ao atualizar a página

    return render(request, 'divisor_app/index.html', context)
