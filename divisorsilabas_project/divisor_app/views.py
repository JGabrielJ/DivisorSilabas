from django.conf import settings
from .analyzer import WordAnalyzer
from django.core.mail import send_mail
from .forms import WordForm, FeedbackForm
from django.shortcuts import render, redirect


def main_view(request):
    word_form = WordForm()
    feedback_form = FeedbackForm()

    result = request.session.pop('result', None)
    error_messages = request.session.pop('error_messages', None)
    feedback_success = request.session.pop('feedback_success', None)

    context = {
        'result': result,
        'word_form': word_form,
        'feedback_form': feedback_form,
        'error_messages': error_messages,
        'feedback_success': feedback_success,
    }

    if request.method == 'POST':
        if 'submit_word' in request.POST:
            word_form = WordForm(request.POST)
            if word_form.is_valid():
                a = WordAnalyzer(word_form.cleaned_data['word'])
                request.session['result'] = {
                    'word': a.word,
                    'tonicity': a.word_stress(),
                    'syl_word': a.get_syllables(),
                    'num_letters': a.count_letters(),
                    'num_phonemes': a.count_phonemes(),
                    'vow_clusters': a.vowel_clusters(),
                    'reversed': a.syllables_backwards(),
                    'num_syllables': a.count_syllables(),
                    'con_clusters': a.consonant_clusters(),
                }
            else:
                request.session['error_messages'] = word_form.errors.get('word')
            return redirect('main-view')

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
                ); request.session['feedback_success'] = "Obrigado pelo seu feedback!"
            return redirect('main-view')

    return render(request, 'divisor_app/index.html', context)
