from optparse import Values
import PySimpleGUI as sg

fundo = 'gray14'
quad = fundo
tam_tela = 350, 600

layout = [[sg.Canvas(size=(120,1), background_color=quad), sg.Text('LOGIN', font='broadway', background_color=fundo, text_color='aqua')],
                [sg.Canvas(size=(350,50), background_color=quad)],

                [sg.Text('ERRO!', background_color=fundo, text_color='red')],

                [sg.Text('Usuário:', background_color=fundo, text_color='yellow', font='callibri', size=(8,1)), sg.Input(size=(30,1))],
                [sg.Text('Senha:', background_color=fundo, text_color='yellow', font='callibri', size=(8,1)), sg.Input(size=(30,1))],
                
                [sg.Canvas(size=(350,1), background_color=quad)],
                [sg.Canvas(size=(90,1), background_color=quad), sg.Button('Não tenho uma conta', button_color='gray20')],
                [sg.Canvas(size=(105,1), background_color=quad), sg.Button('Esqueci a senha', button_color='gray20', disabled=True)],

                [sg.Canvas(size=(172,1), background_color=quad), sg.Button('Voltar', button_color='red', disabled=True), sg.Button('Avançar', button_color='green')]]

window = sg.Window('Tela de Login', layout, size=(tam_tela), background_color=fundo) 

while True:
    event, value = window.read() 
    if event == sg.WINDOW_CLOSED: 
        break

    



