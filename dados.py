#ANALISAR OS DADOS E DAR UM RETORNO (RETURN)

lista = []
def analisa_cadastro(nome, lista, senha1, senha2):
    dados = {}
    
    conta_valida = False
    nome_existe = False
    nome_valido = False
    senha_valida = False

    dados['nome'] = nome.lower().strip()
    print(len(dados['nome']))
    print(dados['nome'])

    recebe_nome = nome
    separa_nome = recebe_nome.split()
    junta_nome = ''.join(separa_nome)

    #analisar se a conta existe
    for pessoa in lista:
        for k, v in pessoa.items():
            if k == 'nome' and v == nome:
                nome_existe = True
            
    if nome_existe == False:
        dados['senha'] = senha1
        if len(nome) >= 5 and len(nome) <= 14 and nome[0].isnumeric() == False and len(recebe_nome) == len(junta_nome) and nome.isspace() == False and nome != '':
            nome_valido = True
        #elif nome.isspace() or nome == '':
            #nome_valido = False
        else:
            nome_valido = False

        if len(senha1) >= 8 and len(senha1) <= 12 and senha1[0].isnumeric():
            if senha1 == senha2:
                senha_valida = True

    # Se o nome e a senha forem validos
    if nome_valido == True and senha_valida == True:
        conta_valida = True

    # Se a conta for valida
    if conta_valida:
        lista.append(dados.copy())

    return conta_valida, lista, senha1
