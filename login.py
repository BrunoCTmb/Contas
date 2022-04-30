from telas import cadastro

class Login():
    def verificar_login(self, nome, senha, lista):
        self.cadastrado = False
        self.login_valido = False

        #verificar se a pessoa existe
        for pessoa in lista:
            for k, v in pessoa.items():
                if k == 'nome' and v == nome:
                    self.cadastrado = True
                    break

        print('ja foi cadastrado:', self.cadastrado)

        if self.cadastrado:
            for pessoa in lista:
                if pessoa['nome'] == nome:
                    if senha == pessoa['senha']:
                        self.login_valido = True

        print('login valido:', self.login_valido)

        return self.cadastrado, self.login_valido
                    