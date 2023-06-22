import smtplib
import PySimpleGUI as sg
from divisor.funct import *
from email.message import Message


class Interface:
    """
    The GUI for the DivisorSilabas program.
    """

    def __init__(self) -> None:
        """
        Initializes the program's GUI.
        """

        sg.theme('DarkBlue17')

        self.layout = [
            [sg.Text('Bem-vindo(a) ao Divisor de Sílabas!', auto_size_text=True, font=('Arial', 12, 'bold'), expand_x=True, justification='center')],
            [sg.HorizontalSeparator(color='#00FF00')],
            [sg.Text('Digite uma palavra:', auto_size_text=True),
             sg.Input(key='word', expand_x=True, text_color='#000000', background_color='#A6B2BE', border_width=2),
             sg.Button('Enviar', target='word', auto_size_button=True, border_width=2)],
            [sg.Text('\n\n\n\n\n\n\n', key='result', auto_size_text=True, text_color='#000000', background_color='#F2D77E', relief=sg.RELIEF_RIDGE, border_width=3, expand_x=True, justification='center')],
            [sg.Text('Dúvidas? Feedbacks? Erros na divisão silábica? Contate-nos!', auto_size_text=True, pad=((0, 0), (25, 0)), expand_x=True, justification='center')],
            [sg.Multiline(key='feedback', border_width=2, auto_size_text=True, expand_x=True, expand_y=True, no_scrollbar=True, rstrip=True)],
            [sg.Button('Enviar feedback', target='feedback', auto_size_button=True, expand_x=True, border_width=2)]
        ]

        self.window = sg.Window('Divisor de Sílabas', self.layout, size=(640, 480), icon='files/icon.ico', resizable=True)


    def update_info(self, word: str) -> None:
        """
        Updates information about the user-supplied word.

        Args:
            word: A string containing the word provided by the user.
        """

        info_list = self.__generate_info(word)
        text = f'Divisão Silábica da Palavra "{info_list["word"].upper()}":\n\n\n{info_list["syl_word"]}\nEla possui {info_list["num_letters"]} letras e {info_list["num_syllables"]} sílabas.\n\n\n'
        self.window['result'].update(text)


    def __generate_info(self, word: str) -> dict[str, int]:
        """
        Generates information about the word provided by the user.

        Args:
            word: A string containing the word provided by the user.

        Returns:
            A dictionary of strings and integers containing
            information about the word provided by the user. For example:

            {
                'word': 'teste',
                'syl_word': 'tes-te',
                'num_letters': 5,
                'num_syllables': 2
            }
        """

        validate = ValidateInfo()
        if validate.check_info(word):
            info_list = validate.success_info(word)
        else:
            info_list = validate.failure_info()

        return info_list


    def send_email(self, text: str) -> None:
        """
        Sends an email containing the user feedback about the program.

        Args:
            text: A string containing the user-written feedback text.
        """

        body: str = f'''
            <p> Olá, João! </p>
            <p> {text} </p>
        '''

        msg = Message()
        msg['Subject'] = 'Dúvidas / Feedbacks / Falhas'
        msg['From'] = 'duvidas.divisor03@gmail.com'
        msg['To'] = 'gjacinto0707@gmail.com'
        password = 'irzemjpxcokaztut'
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(body)

        smtp = smtplib.SMTP('smtp.gmail.com: 587')
        smtp.starttls()
        smtp.login(msg['From'], password)
        smtp.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
        self.window['feedback'].update('Email enviado com sucesso!')


class ValidateInfo:
    """
    The class to validate the info (word) provided by the user.
    """

    def check_info(self, word: str) -> bool:
        """
        Checks that the user-supplied word has only letters.

        Args:
            word: A string containing the word provided by the user.

        Returns:
            A boolean that indicates whether the
            user-supplied word has only letters. For example:

            True -> the word is valid
        """

        if word.isalpha():
            return True
        else:
            return False

    def success_info(self, word: str) -> dict[str, int]:
        """
        When the word provided by the user is valid,
        it provides information about it, such as its
        syllabic division and number of letters and syllables.

        Args:
            word: A string containing the word provided by the user.

        Returns:
            A dictionary of strings and integers containing
            the user-supplied word, your syllabic division and
            total number of letters and syllables. For example:

            {
                'word': 'exemplo',
                'syl_word': 'e-xem-plo',
                'num_letters': 7,
                'num_syllables': 3
            }
        """

        return {
            'word': word,
            'syl_word': divide_word(word),
            'num_letters': count_letters(word),
            'num_syllables': count_syllables(word)
        }


    def failure_info(self) -> dict[str, int]:
        """
        When the word provided by the user is invalid,
        it provides invalidity values against the given word.

        Returns:
            A dictionary of strings and integers containing
            an empty string, an error message and zeros.
        """

        return {
            'word': '',
            'syl_word': 'PALAVRA INVÁLIDA!',
            'num_letters': 0,
            'num_syllables': 0
        }
