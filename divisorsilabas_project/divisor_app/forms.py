from django import forms
from django.http import Http404
from django.conf import settings
from .analyzer import WordAnalyzer
from better_profanity import profanity


profanity.load_censor_words_from_file(settings.RESTRICTED_WORDS_FILE)

class WordForm(forms.Form):
    word = forms.CharField (
        label='Digite uma palavra (no singular)', min_length=2, max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Ex.: divisor'})
    )

    def clean_word(self):
        a = WordAnalyzer(self.cleaned_data['word'])

        if profanity.contains_profanity(a.word):
            raise Http404("Tome cuidado com o que sai da sua boca (*_*)")

        if a.word in settings.EASTER_EGGS.keys():
            raise forms.ValidationError(settings.EASTER_EGGS[a.word])

        if not a.word.isalpha() and '-' not in a.word:
            raise forms.ValidationError("Por favor, digite apenas letras!")

        if not a.word_exists():
            raise forms.ValidationError(f"A palavra \"{a.word.upper()}\" não foi encontrada." \
                                        + " Verifique se ela foi digitada corretamente ou" \
                                        + " se realmente existe no dicionário brasileiro.")

        return a.word


class FeedbackForm(forms.Form):
    feedback = forms.CharField (
        label='Críticas, problemas na busca ou erros na divisão? Contate-nos!',
        widget=forms.Textarea(attrs={'class': 'form-control mt-2', 'rows': 4})
    )
