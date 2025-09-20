import time
from Classes import banco
 
gabriel=banco('Gabriel','03/09/20')
pedro=banco('Pedro','08/10/2028')
joao=banco('Joao','15/10/2009')
Eduardo=banco("Eduardo Chaves da Silva","26/03/2005")

cadastros={1:gabriel,2:pedro,3:joao,4:Eduardo}
while True:
    print("=== Escolha uma conta ===")
    print("[1] Gabriel")
    print("[2] Pedro")
    print("[3] João")
    print("[4] Eduardo")
    print("[5] Encerrar Sistema")
    print("=========================")
    escolha = int(input("Digite a opção: "))

    if escolha in cadastros:
        print()
        cadastros[escolha].consultar()  # abre o menu da conta escolhida
    elif escolha == 5:
        print('Encerrando')
        for i in range(1,4):
            time.sleep(0.20)
            print(i)
        print("Sistema encerrado. 👋")
        break
    else:
        print('Opção Invalida')