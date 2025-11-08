import requests, unicodedata
from bs4 import BeautifulSoup
from urllib.parse import quote


class WordAnalyzer():
    def __init__(self, word: str) -> None:
        """Receives a single word and analyzes it in detail.

        Args:
            word (str): Contains the word provided by the user.
        """
        self.word = word.lower().strip()

        nfkd_form = unicodedata.normalize('NFKD', self.word)
        query_word = ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

        self.response = requests.get(f'https://www.dicio.com.br/{quote(query_word)}/',
                                     headers={'User-Agent': 'Mozilla/5.0'})

    def word_exists(self) -> bool:
        """Checks if a word exists by consulting `www.dicio.com.br`.

        Returns:
            bool: True if the word is found, False otherwise.
        """
        try:
            return self.response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def get_syllables(self) -> str:
        """Gets the syllables of a word by scraping `www.dicio.com.br`.

        Returns:
            str: Contains the syllables of the user-supplied
            word if found, otherwise an empty string.
        """
        try:
            if self.word_exists():
                soup = BeautifulSoup(self.response.content, 'html.parser')
                for p_tag in soup.find_all('p', class_='adicional'):
                    if 'Separação silábica:' in p_tag.text:
                        for b_tag in p_tag.find_all_next('b'):
                            syllables = b_tag.text.replace('-', '').lower().strip()
                            if syllables == self.word.replace('-', ''):
                                return b_tag.text
        except requests.exceptions.RequestException:
            return ''
        return ''

    def join_syllables(self) -> list[str]:
        """Joins the syllables of the user-supplied word into a list of strings.

        Returns:
            list[str]: Contains the user-supplied word divided syllabically.
        """
        return self.get_syllables().split('-')

    def count_syllables(self) -> int:
        """Counts the number of syllables of the user-supplied word.

        Returns:
            int: Indicates the length of the syllables list of the user-supplied word.
        """
        return len(self.join_syllables())

    def count_letters(self) -> int:
        """Counts the number of letters of the user-supplied word.

        Returns:
            int: Indicates the length of the user-supplied word.
        """
        return len(self.word.replace('-', ''))
