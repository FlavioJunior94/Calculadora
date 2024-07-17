from utils import ops
from time import sleep
import calculadora

__name__=='__operacoes_simples__'

def menu_ops():
    print("""
        ================================
        =======ESCOLHA A OPERAÇÃO=======
        ================================
        1 - ADIÇÃO
        2 - SUBTRAÇÃO
        3 - MULTIPLICAÇÃO
        4 - DIVISÃO
        5 - VOLTAR AO MENU PRINCIPAL
        ================================
        """)
    while True:
        try:
            op=int(input('operação: '))
            break
        except:
            print('dado invalido! tente novamente.')

    if op==1:
        num=[]
        while True:
            try:
                cont=int(input('quantos numeros deseja somar ? '))
                break
            except:
                print('dado invalido! tente novamente.')
                continue
        for i in range(1, cont+1):
            num.append(float(input(f'{i}º numero: ')))
        ops.soma(num)
        sleep(1.8)
        menu_ops()
    elif op==2:
        ops.subtr()
        sleep(1.8)
        menu_ops()
    elif op==3:
        ops.multi()
        sleep(1.8)
        menu_ops()
    elif op==4:
        ops.divi()
        sleep(1.8)
        menu_ops()
    elif op==5:
        calculadora.menu()
    else:
        print("opção invalida!")
        sleep(1.8)
        menu_ops()


