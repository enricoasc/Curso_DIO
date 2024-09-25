from datetime import datetime
import os
import locale
## criar um objeto com os dados da conta 

__USUARIOS__ = dict()
__CONTAS__ = 0

class Conta_bancaria:
    def __init__(self):
        self.saldo = 0
        self.QTD_DIARIA_LIMITE = 3
        self.VALOR_DIARIA_LIMITE = 1000
        self.numero_de_saques = 0
        self.num_conta=0
        self.log_extrato = ' -> \033[94m ..: SEM LANÇAMENTOS ATÉ AGORA :.. \033[0m '
        
## funçao depositar dentro do objeto ###############################

    def depositar(self):
        data_atual=datetime.now().strftime('%d/%m/%Y')
        valor_deposito = ''
        mensagem = ''

        while type(valor_deposito) != float:

            valor_deposito = input('\ndigite o valor de depósito .: ')

            try:

                if float(valor_deposito) > 0:
                    valor_deposito = float(valor_deposito)
                else:
                    print('\n\n \033[91mValor incorreto ! Tente outra vez ...  \033[0m')    

            except ValueError:
                print('\n\n \033[91mValor incorreto ! Tente outra vez ...  \033[0m')


        self.saldo += valor_deposito
        self.limpa_log()
        self.log_extrato += f'--> (D) {data_atual} | \033[92m R$ {valor_deposito:.2f} \033[0m \n'

        
        mensagem += '\n'+'-'*28
        mensagem += f'\n -> Valor R$ {valor_deposito:.2f} depositado com sucesso! \n'
        mensagem += '-'*28

        lc()
        print('\033[93m'+mensagem+'\033[0m')

## função sacar dentro do objeto ###############################
    def sacar(self):
        data_atual=datetime.now().strftime('%d/%m/%Y')
        valor_saque = ''
        mensagem = ''

        while type(valor_saque) != float:

            valor_saque = input('\ndigite o valor de saque .: ')

            try:

                if float(valor_saque) > 0:
                    valor_saque = float(valor_saque)
                else:
                    print('\n\n \033[91mValor incorreto ! Tente outra vez ...  \033[0m')    

            except ValueError:
                print('\n\n \033[91mValor incorreto ! Tente outra vez ...  \033[0m')        
        
        if valor_saque > self.VALOR_DIARIA_LIMITE :
            print(f'\n ||.. \033[91mValor de saque maior que o LIMIT DIÁRIO R$ {self.VALOR_DIARIA_LIMITE} ..||\033[0m \n\n')
            return

        if self.numero_de_saques >= self.QTD_DIARIA_LIMITE:
            print('\n ||.. \033[91mLimiti diário de saques atingido, favor volte outro dia ..||\033[0m \n\n')
            return
        
        if valor_saque > self.saldo:
            print(f'\n ||.. \033[91mValor de saque maior que o saldo disponível R$ {self.saldo:.2f} ..||\033[0m \n\n')
            return            

        self.saldo -= valor_saque
        self.numero_de_saques += 1 
        self.limpa_log()
        self.log_extrato += f'--> (S) {data_atual} | \033[91m R$ {valor_saque:.2f} \033[0m \n'        

        mensagem += '\n'+'-'*28
        mensagem += f'\n -> Valor R$ {valor_saque:.2f} retirado com sucesso ! \n'
        mensagem += '-'*28

        lc()
        print('\033[93m'+mensagem+'\033[0m')


## função extrato dentro do objeto
    def extrato(self):
        data_atual=datetime.now().strftime('%d/%m/%Y')
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
        data_hoje = datetime.now()
        data_extenso = data_hoje.strftime('%A, %d de %B de %Y')
        
        lc()
        msg_extrato = f"""
--------------------------------------------
*********     EXTRATO DA CONTA     *********
Numero da Conta : {self.num_conta},
Olá, 
Agradecemos por usar nosso BancoPython!!

\033[96m {data_extenso}\033[0m
--------------------------------
{self.log_extrato}
================================
\033[93m Total -> R$ {self.saldo:.2f} \033[0m
--------------------------------

\033[95m Tenha um ótimo dia !! \033[0m
                      """
        print(msg_extrato)
        
    def criar_conta(self):
        # nova_conta = Conta_bancaria
        global __CONTAS__

        __CONTAS__ += 1
        self.num_conta = __CONTAS__
        return self


    def limpa_log(self):
        if 'SEM LANÇAMENTOS ATÉ AGORA' in self.log_extrato:
            self.log_extrato = ''

# ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

class Usuario:
    def __init__(self):
        self.cpf =''
        self.nome =''
        self.endereco =''
        self.nascimento =''
    
    def criar_usuario(self):
        lc()
        self.cpf = input('Informe o CPF do Usuario.:')
        global __USUARIOS__

        if self.cpf in __USUARIOS__.keys():
            lc()
            print(' .. usuario ja cadastrado ..')
            return 
        else:
            self.nome = input('Informe o Nome do Usuario.:')
            self.nascimento = input('Informe o Data Nascimento do Usuario.:')
            self.endereco = input('Informe o Endereço do Usuario.:')

            conta=[]
            dict_dados = {'nome':self.nome, 'endereco':self.endereco, 'nascimento':self.nascimento, 'contas':conta}
            dict_usuario = {self.cpf : dict_dados}
            
            __USUARIOS__.update(dict_usuario) 
            print( ".. usuario cadastrado com Sucesso !! ..")

class lc:
        def __init__(self):
            # Detecta o sistema operacional e executa o comando apropriado
            if os.name == 'nt':  # Se for Windows
                os.system('cls')
            else:  # Se for Linux ou macOS
                os.system('clear')

class Valida:
    def __init__(self):
        pass

    def operacao(self,nome_operacao):
        global __USUARIOS__
        if  nome_operacao == 'criar_usuario':
            lc()
            Usuario().criar_usuario()
            return
        
        elif nome_operacao == 'criar_conta':
            lc()
            cpf_usuario= input('Digite o CPF do Titular ..: ')
            if cpf_usuario in __USUARIOS__.keys():
                nova_conta = Conta_bancaria()
                nova_conta = nova_conta.criar_conta()
                __USUARIOS__[cpf_usuario]['contas'].append(nova_conta)
                # print(__USUARIOS__[cpf_usuario]['contas'])
                print(' ::.. Conta bancária cadastrada com sucesso !! ..:: ')
            else:
                lc()
                print(' ::.. Usuario inexistente , favor cadastrar usuario antes de criar conta bancária ..:: ')
        else:  
            lc()
            cpf_usuario= input('Digite o CPF do Titular  ..:')
            conta_titular=''
            if cpf_usuario in __USUARIOS__.keys():
                num_conta_tela= input('Digite o Numero da Conta do Titular ..: ')
                for indice , conta_usuario in enumerate(__USUARIOS__[cpf_usuario]['contas']):
                    if str(conta_usuario.num_conta) == num_conta_tela:
                        conta_titular = __USUARIOS__[cpf_usuario]['contas'][indice]
                        # conta_titular.nome_operacao()
                        # Usa getattr para obter o método da classe baseado no nome da operação
                        metodo = getattr(conta_titular, nome_operacao, None)
                        if callable(metodo):
                            return metodo()
                        else:
                            return "Operação inválida"
                        
                if conta_titular == '':
                        print(':.. Conta não encontrada , favor cadastrar uma nova conta ..: ')
            else:
                print('..: Usuário não encontado, favor cadastrar um novo usuario :.. ')

        return


############################################################################################################
############################################################################################################

## menu em loop fora do objeto na __main__ 
operacao_usuario = Valida() 
menu = """
            =======================================
               **  Bem Vindo ao BancoPython !  ** 
            ---------------------------------------
            Lista de opções: 
                    - 'S' Sacar:
                    - 'D' Depositar:
                    - 'E' Ver extrato:
                    - 'C' Criar Conta
                    - 'U' Criar Uusario
                    - 'Q' Sair
            Insira a opção desejada :
        """
while True:
    opcao = input(menu)

    if opcao.upper() == 'S':
        operacao_usuario.operacao(nome_operacao='sacar')

    elif opcao.upper() == 'D':
        operacao_usuario.operacao(nome_operacao='depositar')

    elif opcao.upper() == 'E':
        operacao_usuario.operacao(nome_operacao='extrato')

    elif opcao.upper() == 'Q':
        break
    
    elif opcao.upper() == 'U':
        operacao_usuario.operacao(nome_operacao='criar_usuario')

    elif opcao.upper() == 'C':
        operacao_usuario.operacao(nome_operacao='criar_conta')

    else: 
        lc()
        print('\n ..: Opção incorreta , tente novamente ..: \n')