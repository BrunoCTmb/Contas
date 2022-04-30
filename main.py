# NECESSÁRIO:
# informar qual erro ocorreu ao cadastrar ou entrar na conta 
    # tentar exibir a mesma tela de cadastro, porém com um texto do erro que ocorreu 

# explorar mais os o arquivo 'dados.py'
# tentar exibir uma tela com todas as contas ( tentar um 'loop for' )


import PySimpleGUI as sg
import telas
import dados
from login import Login

login_inicial, cadastro_inicial, cadastro_concluido, cadastro_invalido, login_concluido, login_invalido = telas.login_inicial(), None, None, None, None, None

todos_dados = []

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        break

    # LOGIN
    #quando o usuario digitar os dados para entrar
    if window == login_inicial or window == login_invalido and event == 'Avançar':
        verif = Login().verificar_login(values[0], values[1], todos_dados)
        if verif[1]:
            login_inicial.hide()
            login_concluido = telas.login_efetuado()
        else:
            login_inicial.hide()
            login_invalido = telas.login_erro()

    #se der erro no login e colocar para cadadstrar uma conta
    if window == login_invalido and event == 'Não tenho uma conta':
        login_invalido.hide()
        cadastro_inicial = telas.cadastro()

    #de login inicial  para cadastrar uma conta
    if window == login_inicial and event == 'Não tenho uma conta':
        login_inicial.hide()
        cadastro_inicial = telas.cadastro()




    # CADASTRO
    #de cadastrar conta para login inicial
    if window == cadastro_inicial and event == 'Voltar':
        cadastro_inicial.hide()
        login_inicial.un_hide()

        
    #quando 'cadastrar' uma conta e clicar em 'avançar'
    if window == cadastro_inicial and event == 'Avançar':
        conta_valida = dados.analisa_cadastro(values[0].lower(), todos_dados, values[1], values[2])
        #posicao 0: conta valida ou nao, posicao 1: lista de nomes
        print(conta_valida)
        print('lista de dados:', todos_dados)
        if conta_valida[0] == True:
            cadastro_inicial.hide()
            cadastro_concluido = telas.cadastro_efetuado()
        elif conta_valida[0] == False:
            cadastro_inicial.hide()
            cadastro_invalido = telas.cadastro_erro()


    #quando for 'cadastrada' com 'sucesso'
    if window == cadastro_concluido and event == 'Avançar':
        cadastro_concluido.hide()
        login_inicial.un_hide()

    #quando a conta for 'invalida'
    if window == cadastro_invalido and event == 'Avançar':
        cadastro_invalido.hide()
        login_inicial.un_hide()
        

            
        
        



#TELAS:
# login_inicial - LAYOUT
# login_efetuado
# login_erro

# cadastro_inicial - LAYOUT
# cadastro_efetuado
# cadastro_erro