from hyphen import Hyphenator
from abc import ABC, abstractmethod


def divide_word(word: str) -> str:
    """
    Separates the syllables of the
    user-supplied word into a single string.

    Args:
        word: A string containing the word provided by the user.

    Returns:
        A string containing the user-supplied
        word divided syllabically. For example:

        syl_word = 'e-xem-plo'
    """

    syllables = get_syllables(word.lower())
    syl_word = '-'.join(syllables)
    return syl_word


def count_syllables(word: str) -> int:
    """
    Counts the number of syllables of the user-supplied word.

    Args:
        word: A string containing the word provided by the user.

    Returns:
        An integer that indicates the length of the
        syllables list of the user-supplied word. For example:

        len(syllables) = 3
    """

    syllables = get_syllables(word.lower())
    return len(syllables)


def count_letters(word: str) -> int:
    """
    Counts the number of letters of the user-supplied word.

    Args:
        word: A string containing the word provided by the user.

    Returns:
        An integer that indicates the length
        of the user-supplied word. For example:

        len(word) = 7
    """

    return len(word)


def check_word(word: str) -> bool:
    """
    Checks if the user-supplied word contains only letters
    or is in the list of words that aren't correctly separated.

    Args:
        word: A string containing the word provided by the user.

    Returns:
        A boolean that indicates if the user-supplied word
        is correctly separated or not. For example:

        cond = False -> the word is correctly separated
    """

    failures = open('files/failures.txt', 'rt', encoding='UTF-8')
    fail_words = failures.read().split('\n')
    cond = True if word in fail_words or not word.isalpha() else False
    return cond


def get_syllables(word: str) -> list[str]:
    """
    Gets the syllables of the user-supplied word.

    Args:
        word: A string containing the word provided by the user.

    Returns:
        A list of strings containing the syllables
        of the user-supplied word. For example:

        syllables = ['e', 'xem', 'plo']
    """

    h = Hyphenator('pt_BR')
    cond = check_word(word)

    if not cond:
        syllables = h.syllables(word)
        if syllables == []:
            syllables.append(word)
    else:
        subclasses = {'amor': Amor(), 'exemplo': Exemplo(), 'otorrinolaringologista': Otorrinolaringologista(), 'pneumoultramicroscopicossilicovulcanoconiótico': Pneumoultramicroscopicossilicovulcanoconiotico()}
        wrong_word = subclasses[word] if word in subclasses.keys() else Other()
        syllables = wrong_word.fix()

    return syllables


class PalavraErrada(ABC):
    """
    The interface for misspelled words
    that may appear in program.
    """

    @abstractmethod
    def fix(self) -> None:
        """
        Initializes an abstract method
        for subclasses to fix misspelled words.
        """

        pass


class Amor(PalavraErrada):
    """
    The subclass of the PalavraErrada class
    that fixes the syllables of the word 'amor'.
    """

    def fix(self) -> list[str]:
        """
        Fixes the syllables of the word 'amor'.

        Returns:
            A list of strings containing the syllables of the word 'amor'.
        """

        return ['a', 'mor']


class Exemplo(PalavraErrada):
    """
    The subclass of the PalavraErrada class
    that fixes the syllables of the word 'exemplo'.
    """

    def fix(self) -> list[str]:
        """
        Fixes the syllables of the word 'exemplo'.

        Returns:
            A list of strings containing the syllables of the word 'exemplo'.
        """

        return ['e', 'xem', 'plo']


class Otorrinolaringologista(PalavraErrada):
    """
    The subclass of the PalavraErrada class
    that fixes the syllables of the word 'otorrinolaringologista'.
    """

    def fix(self) -> list[str]:
        """
        Fixes the syllables of the
        word 'otorrinolaringologista'.

        Returns:
            A list of strings containing the syllables
            of the word 'otorrinolaringologista'.
        """

        return ['o', 'tor', 'ri', 'no', 'la', 'rin', 'go', 'lo', 'gis', 'ta']


class Pneumoultramicroscopicossilicovulcanoconiotico(PalavraErrada):
    """
    The subclass of the PalavraErrada class
    that fixes the syllables of the word
    'pneumoultramicroscopicossilicovulcanoconiótico'.
    """

    def fix(self) -> list[str]:
        """
        Fixes the syllables of the word
        'pneumoultramicroscopicossilicovulcanoconiótico'.

        Returns:
            A list of strings containing the syllables of the word
            'pneumoultramicroscopicossilicovulcanoconiótico'.
        """

        return ['pneu', 'mo', 'ultra', 'mi', 'cros', 'co', 'pi', 'cos', 'si', 'li', 'co', 'vul', 'ca', 'no', 'co', 'ni', 'ó', 'ti', 'co']


class Other(PalavraErrada):
    """
    The subclass of the PalavraErrada class
    that fixes any strings that aren't valid words.
    """

    def fix(self) -> list:
        """
        Fixes any strings that aren't valid words.

        Returns:
            A empty list.
        """

        return []
