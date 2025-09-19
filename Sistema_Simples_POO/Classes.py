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
            print('[5] = Encerrar Sistema')
            print('============================')
            valor=int(input('Digite a opção: '))
            print()
            if valor == 1:
                print('Nome: ',self.nome)
                print()
            elif valor == 2:
                print('Data de Nascimento: ',self.data)
                print()
            elif valor == 3:
                print('Saldo: ',f'{self.saldo}$')
                print()
            elif valor == 4:
                valor=int(input('Informe o valor do deposito: '))
                self.saldo=self.saldo+valor
                print()
                print('----------------------------')
                print('Novo saldo',f'{self.saldo}$')
                print('----------------------------')
                print()
            elif valor == 5:
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
 
