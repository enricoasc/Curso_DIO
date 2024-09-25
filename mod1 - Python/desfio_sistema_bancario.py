from datetime import datetime
import os
import locale
## criar um objeto com os dados da conta 

class Conta_bancaria:
    def __init__(self,nome):
        self.saldo = 0
        self.QTD_DIARIA_LIMITE = 3
        self.VALOR_DIARIA_LIMITE = 1000
        self.numero_de_saques = 0
        self.nome=nome
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

        self.lc()
        print('\033[93m'+mensagem+'\033[0m')

## função sacar dentro do objeto ###############################
    def sacar(self):
        data_atual=datetime.now().strftime('%d/%m/%Y')
        valor_saque = ''
        mensagem = ''

        while type(valor_saque) != float:

            valor_saque = input('\ndigite o valor de depósito .: ')

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

        self.lc()
        print('\033[93m'+mensagem+'\033[0m')


## função extrato dentro do objeto
    def extrato(self):
        data_atual=datetime.now().strftime('%d/%m/%Y')
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
        data_hoje = datetime.now()
        data_extenso = data_hoje.strftime('%A, %d de %B de %Y')
        
        self.lc()
        msg_extrato = f"""
--------------------------------------------
*********     EXTRATO DA CONTA     *********

Olá {self.nome},
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
        


    def lc(self):
        # Detecta o sistema operacional e executa o comando apropriado
        if os.name == 'nt':  # Se for Windows
            os.system('cls')
        else:  # Se for Linux ou macOS
            os.system('clear')

    def limpa_log(self):
        if 'SEM LANÇAMENTOS ATÉ AGORA' in self.log_extrato:
            self.log_extrato = ''



## menu em loop fora do objeto na __main__ 
conta = Conta_bancaria('Enrico A. S. Card') 
menu = """
            =======================================
               **  Bem Vindo ao BancoPython !  ** 
            ---------------------------------------
            Lista de opções: 
                    - 'S' Sacar:
                    - 'D' Depositar:
                    - 'E' Ver extrato:
                    - 'Q' Sair
            Insira a opção desejada :
        """
while True:
    opcao = input(menu)

    if opcao.upper() == 'S':
        conta.sacar()

    elif opcao.upper() == 'D':
        conta.depositar()

    elif opcao.upper() == 'E':
        conta.extrato()

    elif opcao.upper() == 'Q':
        break
    else: 
        conta.lc()
        print('\n ..: Opção incorreta , tente novamente ..: \n')