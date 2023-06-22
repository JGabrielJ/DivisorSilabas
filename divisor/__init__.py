import PySimpleGUI as sg
from divisor.interf import Interface


def init() -> None:
    """
    Initializes the GUI for all program operation.
    """

    screen = Interface()
    while True:
        screen.event, screen.values = screen.window.Read()

        if screen.event == sg.WIN_CLOSED:
            break

        if screen.event == 'Enviar':
            screen.update_info(screen.values['word'])

        if screen.event == 'Enviar feedback':
            screen.send_email(screen.values['feedback'])
