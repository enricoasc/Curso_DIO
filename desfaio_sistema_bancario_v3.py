from abc import ABC, abstractmethod
from datetime import datetime
import os

class Usuario:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def executar_transacao(self, conta, operacao):
        operacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaJuridica(Usuario):
    def __init__(self, nome_fantasia, data_abertura, cnpj, endereco):
        super().__init__(endereco)
        self.nome_fantasia = nome_fantasia
        self.data_abertura = data_abertura
        self.cnpj = cnpj

class ContaBancaria:
    def __init__(self, numero_conta, usuario):
        self._saldo = 0
        self._numero_conta = numero_conta
        self._agencia = "0022"
        self._usuario = usuario
        self._registro = Registro()

    @classmethod
    def criar_conta(cls, usuario, numero_conta):
        return cls(numero_conta, usuario)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def usuario(self):
        return self._usuario

    @property
    def registro(self):
        return self._registro

    def retirar(self, quantia):
        saldo_atual = self.saldo
        saldo_insuficiente = quantia > saldo_atual

        if saldo_insuficiente:
            print("\033[91m\n@@@ Operação falhou! Saldo insuficiente. @@@\033[0m")

        elif quantia > 0:
            self._saldo -= quantia
            print("\033[92m\n=== Saque efetuado com sucesso! ===\033[0m")
            return True

        else:
            print("\033[91m\n@@@ Operação falhou! Quantia inválida. @@@\033[0m")

        return False

    def adicionar_fundos(self, quantia):
        if quantia > 0:
            self._saldo += quantia
            print("\033[92m\n=== Depósito efetuado com sucesso! ===\033[0m")
        else:
            print("\033[91m\n@@@ Operação falhou! Quantia inválida. @@@\033[0m")
            return False

        return True

class ContaEmpresarial(ContaBancaria):
    def __init__(self, numero_conta, usuario, limite_saque=1000, max_saques_diarios=5):
        super().__init__(numero_conta, usuario)
        self.limite_saque = limite_saque
        self.max_saques_diarios = max_saques_diarios

    def retirar(self, quantia):
        saques_efetuados = len(
            [op for op in self.registro.transacoes if op["tipo"] == Retirada.__name__]
        )

        limite_excedido = quantia > self.limite_saque
        saques_maximos_excedidos = saques_efetuados >= self.max_saques_diarios

        if limite_excedido:
            print("\033[91m\n@@@ Operação falhou! Quantia excede o limite permitido. @@@\033[0m")

        elif saques_maximos_excedidos:
            print("\033[91m\n@@@ Operação falhou! Número máximo de saques excedido. @@@\033[0m")

        else:
            return super().retirar(quantia)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            Conta:\t\t{self.numero_conta}
            Titular:\t{self.usuario.nome_fantasia}
        """

class Registro:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_operacao(self, operacao):
        self._transacoes.append(
            {
                "tipo": operacao.__class__.__name__,
                "valor": operacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

class Operacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(self, conta):
        pass

class Retirada(Operacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.retirar(self.valor)

        if sucesso:
            conta.registro.adicionar_operacao(self)

class AdicionarFundos(Operacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.adicionar_fundos(self.valor)

        if sucesso:
            conta.registro.adicionar_operacao(self)

class lc:
        def __init__(self):
            # Detecta o sistema operacional e executa o comando apropriado
            if os.name == 'nt':  # Se for Windows
                os.system('cls')
            else:  # Se for Linux ou macOS
                os.system('clear')
        def __del__(self):
            pass
# Funções auxiliares para o menu
usuarios = []
contas = []

def criar_usuario():
    lc()
    nome_fantasia = input("Digite o nome fantasia: ")
    lc()
    data_abertura = input("Digite a data de abertura (dd/mm/aaaa): ")
    lc()
    cnpj = input("Digite o CNPJ: ")
    lc()
    endereco = input("Digite o endereço: ")
    lc()
    usuario = PessoaJuridica(nome_fantasia, data_abertura, cnpj, endereco)
    usuarios.append(usuario)
    lc()
    print("\033[92m\nUsuário criado com sucesso!\033[0m")

def criar_conta():
    lc()
    if not usuarios:
        print("\033[91m\nNenhum usuário encontrado. Crie um usuário primeiro.\033[0m")
        return
    print("\nUsuários disponíveis:")
    for i, usuario in enumerate(usuarios):
        print(f"{i + 1}. {usuario.nome_fantasia}")
    usuario_index = int(input("Selecione o usuário (número): ")) - 1
    numero_conta = input("Digite o número da conta: ")
    lc()
    conta = ContaEmpresarial.criar_conta(usuarios[usuario_index], numero_conta)
    usuarios[usuario_index].adicionar_conta(conta)
    contas.append(conta)
    print("\033[92m\nConta criada com sucesso!\033[0m")

def sacar():
    lc()
    if not contas:
        print("\033[91m\nNenhuma conta encontrada. Crie uma conta primeiro.\033[0m")
        return
    print("\nContas disponíveis:")
    for i, conta in enumerate(contas):
        print(f"{i + 1}. Conta: {conta.numero_conta}, Titular: {conta.usuario.nome_fantasia}")
    try:
        conta_index = int(input("Selecione a conta (número): ")) - 1
        valor = float(input("Digite o valor a ser sacado: "))
        lc()
        retirada = Retirada(valor)
        contas[conta_index].usuario.executar_transacao(contas[conta_index], retirada)
    except:
        print( 'valor digitado errado, tente novamente ')
    

def depositar():
    lc()
    if not contas:
        print("\033[91m\nNenhuma conta encontrada. Crie uma conta primeiro.\033[0m")
        return
    print("\nContas disponíveis:")
    for i, conta in enumerate(contas):
        print(f"{i + 1}. Conta: {conta.numero_conta}, Titular: {conta.usuario.nome_fantasia}")
    try:
        conta_index = int(input("Selecione a conta (número): ")) - 1
        valor = float(input("Digite o valor a ser depositado: "))
        lc()
        deposito = AdicionarFundos(valor)
        contas[conta_index].usuario.executar_transacao(contas[conta_index], deposito)
    except:
        print('Numero digitado errado , tente novamente !')

def extrato():
    lc()
    if not contas:
        print("\033[91m\nNenhuma conta encontrada. Crie uma conta primeiro.\033[0m")
        return
    print("\nContas disponíveis:")
    for i, conta in enumerate(contas):
        print(f"{i + 1}. Conta: {conta.numero_conta}, Titular: {conta.usuario.nome_fantasia}")
    try:
        conta_index = int(input("Selecione a conta (número): ")) - 1
        lc()
        print("\nExtrato da Conta:")
        for transacao in contas[conta_index].registro.transacoes:
            print(f"{transacao['data']}: {transacao['tipo']} de R${transacao['valor']}")

        print('='*38+f'\nSaldo:\t\t{contas[conta_index].saldo}')
    except:
        print('Valor digitado incorreto, tente novamente !')
# Menu principal
def menu():
    while True:
        print("\n\033[94mMenu Principal\033[0m")
        print("1. Criar Usuário")
        print("2. Criar Conta")
        print("3. Sacar")
        print("4. Depositar")
        print("5. Extrato")
        print("6. Sair")
        opcao = input("Selecione uma opção: ")

        if opcao == '1':
            criar_usuario()
        elif opcao == '2':
            criar_conta()
        elif opcao == '3':
            sacar()
        elif opcao == '4':
            depositar()
        elif opcao == '5':
            extrato()
        elif opcao == '6':
            break


# Chama o menu principal
if __name__ == "__main__":
    lc()
    menu()
