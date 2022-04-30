import PySimpleGUI as sg

tam_tela = 350, 600
fundo = 'gray14'
quad = fundo

def login_inicial():
    layout = [  [sg.Canvas(size=(120,1), background_color=quad), sg.Text('LOGIN', font='broadway', background_color=fundo, text_color='aqua')],
                [sg.Canvas(size=(350,50), background_color=quad)],

                [sg.Text('Usuário:', background_color=fundo, text_color='yellow', font='callibri', size=(8,1)), sg.Input(size=(30,1))],
                [sg.Text('Senha:', background_color=fundo, text_color='yellow', font='callibri', size=(8,1)), sg.Input(size=(30,1), password_char='*')],
                
                [sg.Canvas(size=(350,1), background_color=quad)],
                [sg.Canvas(size=(90,1), background_color=quad), sg.Button('Não tenho uma conta', button_color='gray20')],
                [sg.Canvas(size=(105,1), background_color=quad), sg.Button('Esqueci a senha', button_color='gray20', disabled=True)],

                #botoes voltar e avancar
                #[sg.Canvas(size=(350,100), background_color=quad)],
                [sg.Canvas(size=(172,1), background_color=quad), sg.Button('Voltar', button_color='red', disabled=True), sg.Button('Avançar', button_color='green')]]

    return sg.Window('Cadastro', layout=layout, finalize=True, size=(tam_tela), background_color=fundo)

def cadastro():
    layout = [  [sg.Canvas(size=(100,1), background_color=quad), sg.Text('CADASTRO', font='broadway', background_color=fundo, text_color='aqua')],
                [sg.Canvas(size=(350,50), background_color=quad)],
                
                [sg.Text('Usuário:', background_color=fundo, text_color='yellow', font='callibri', size=(8,1)), sg.Input(size=(20,1))],
                [sg.Canvas(size=(600,10), background_color=quad)],

                [sg.Text('Senha:', background_color=fundo, text_color='yellow', font='callibri', size=(8,1)), sg.Input(size=(14,1), password_char='*')],
                [sg.Text('Confirme:', background_color=fundo, text_color='yellow', font='callibri', size=(8,1)), sg.Input(size=(14,1), password_char='*')],
                
                [sg.Canvas(size=(172,1), background_color=quad), sg.Button('Voltar', button_color='red'), sg.Button('Avançar', button_color='green')]]


    return sg.Window('Cadastro', layout=layout, finalize=True, size=(tam_tela), background_color=fundo)


def cadastro_efetuado():
    layout = [  [sg.Canvas(size=(350,200), background_color=fundo)],
                [sg.Canvas(size=(25,1), background_color=quad), sg.Text('CADASTRO CONCLUÍDO COM SUCESSO!', background_color=fundo, text_color='green', font='impact')],
                
                [sg.Canvas(size=(350,300), background_color=quad)],
                [sg.Canvas(size=(225,1), background_color=quad), sg.Button('Avançar', button_color='green')]]

    return sg.Window('Cadastro Concluído', layout=layout, finalize=True, size=(tam_tela), background_color=fundo)
    


def cadastro_erro():
    layout = [  [sg.Canvas(size=(350,200), background_color=fundo)],
                [sg.Canvas(size=(85,1), background_color=quad), sg.Text('CADASTRO INVÁLIDO!', background_color=fundo, text_color='red', font='impact')],
                
                [sg.Canvas(size=(350,300), background_color=quad)],
                [sg.Canvas(size=(225,1), background_color=quad), sg.Button('Avançar', button_color='green')]]


    return sg.Window('ERRO', layout=layout, finalize=True, size=(tam_tela), background_color=fundo)


def login_efetuado():
    layout = [  [sg.Text('Login efetuado!', background_color=fundo, text_color='green')],
    
                [sg.Canvas(size=(225,1), background_color=quad), sg.Button('Avançar', button_color='green')]]

    return sg.Window('ERRO', layout=layout, finalize=True, size=(tam_tela), background_color=fundo)


def login_erro():
    layout = [[sg.Canvas(size=(120,1), background_color=quad), sg.Text('LOGIN', font='broadway', background_color=fundo, text_color='aqua')],
                [sg.Canvas(size=(350,24), background_color=quad)],

                [sg.Text('ERRO! Usuário não cadastrado ou senha inválida!', background_color=fundo, text_color='red')],

                [sg.Text('Usuário:', background_color=fundo, text_color='yellow', font='callibri', size=(8,1)), sg.Input(size=(30,1))],
                [sg.Text('Senha:', background_color=fundo, text_color='yellow', font='callibri', size=(8,1)), sg.Input(size=(30,1))],
                
                [sg.Canvas(size=(350,1), background_color=quad)],
                [sg.Canvas(size=(90,1), background_color=quad), sg.Button('Não tenho uma conta', button_color='gray20')],
                [sg.Canvas(size=(105,1), background_color=quad), sg.Button('Esqueci a senha', button_color='gray20', disabled=True)],

                [sg.Canvas(size=(172,1), background_color=quad), sg.Button('Voltar', button_color='red', disabled=True), sg.Button('Avançar', button_color='green')]]

    return sg.Window('ERRO', layout=layout, finalize=True, size=(tam_tela), background_color=fundo)