import time
class banco():
    def __init__(self,nome,data):
        self.nome=nome
        self.data=data
        self.saldo=0

    def consultar(self):
        while True:
            print('===🏦 SISTEMA BANCÁRIO 🏦===')
            print('[1] = Consultar Nome')
            print('[2] = Consultar Data')
            print('[3] = Consultar saldo')
            print('[4] = Realizar um deposito:')
            print('[5] = Sacar Dinheiro')
            print('[6] = Encerrar sistema')
            print('============================')
            valor=int(input('Digite a opção: '))
            print()
            if valor == 1:
                print('Nome: ',self.nome)
                time.sleep(1)
                print()
            elif valor == 2:
                print('Data de Nascimento: ',self.data)
                time.sleep(1)
                print()
            elif valor == 3:
                print('Saldo: ',f'{self.saldo}$')
                print()
                time.sleep(1)
                print()
            elif valor == 4:
                valor=int(input('Informe o valor do deposito: '))
                self.saldo=self.saldo+valor
                print()
                print('----------------------------')
                print('Novo saldo',f'{self.saldo}$')
                print('----------------------------')
                time.sleep(1)
                print()
            elif valor == 5:
                sacar=int(input("Informe quanto desejar sacar: "))
                if self.saldo >= sacar:
                    self.saldo=self.saldo-sacar
                    print()
                    print("Novo Saldo:",self.saldo)
                    print()
                    time.sleep(1)
                else:
                    print()
                    print("Dinheiro Insuficiente")
                    print()
            elif valor == 6:
                print('Encerrando')
                for i in range(1,4):
                    time.sleep(0.20)
                    print(i)
                print("Sistema encerrado. 👋")
                print()
                break
            else:
                print('Opçãp Invilida.')
                print()
 
