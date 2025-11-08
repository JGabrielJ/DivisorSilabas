from django import forms
from .analyzer import WordAnalyzer


class WordForm(forms.Form):
    word = forms.CharField (
        label='Digite uma palavra', min_length=2, max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Ex.: divisor'})
    )

    def clean_word(self):
        a = WordAnalyzer(self.cleaned_data['word'])

        if not a.word.isalpha() and '-' not in a.word:
            raise forms.ValidationError("Por favor, digite apenas letras!")

        # if 'Matrix' == a.word.title():
        #     raise forms.ValidationError("Você encontrou um easter egg!")

        if not a.word_exists():
            raise forms.ValidationError(f"A palavra \"{a.word.upper()}\" não foi encontrada." +\
                                        " Verifique se ela foi digitada corretamente ou" +\
                                        " se realmente existe no dicionário brasileiro.")

        return a.word


class FeedbackForm(forms.Form):
    feedback = forms.CharField (
        label='Problemas com a busca ou inconsistências na divisão? Contate-nos!',
        widget=forms.Textarea(attrs={'class': 'form-control mt-2', 'rows': 4})
    )
