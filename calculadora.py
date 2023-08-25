from utils import ops
from models import operacoes_simples, conversor_base
from time import sleep
def menu():
    print("""
        ================================
        ==========CALCULADORA ==========
        ================================
        =======ESCOLHA A OPERAÇÃO=======
        ================================
        1 - OPERAÇÕES SIMPLES ( + - * / )
        2 - CONVERSOR BASE ( BINARIO, HEXAGONAL, ETC...)
        3 - CONVERSOR DE MOEDA
        4 - BASKARA
        5 - FECHAR CALCULADORA
        ================================
        """)
    while True:
        try:
            op=int(input('operação: '))
            break
        except:
            print('dado invalido! tente novamente.')

    if op==1:
        operacoes_simples.menu_ops()
    if op==2:
        conversor_base.menu_base()
    if op==3:
        pass
    if op==4:
        pass
    if op==5:
        pass
    
    else:
        print('valor invalido, por favor tente novamente!')
        sleep(1)
        menu()

if __name__=='__main__':
    menu()


