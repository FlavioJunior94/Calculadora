from models import operacoes_simples, conversor_base, gerador_senha
from time import sleep
def menu():
    print("""
        =========-=======================
        ==========CALCULADORA ==========
        ================================
        =======ESCOLHA A OPERAÇÃO=======
        ================================
        1 - OPERAÇÕES SIMPLES( +-*/ )
        2 - CONVERSOR BASE
        3 - CONVERSOR DE MOEDA
        4 - BASKARA
        5 - FECHAR CALCULADORA
        6 - GERADOR DE SENHAS
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
        print('\n Volte sempre ! :)')
        exit()
    if op==6:
        while True:
            try:
                tam_senha=int(input('Insira o tamanho da sua senha: '))
                break
            except:
                print('dado invalido! tente novamente.')
        gerador_senha.gerador_senha(tam_senha)
        sleep(1)
        menu()
    else:
        print('valor invalido, por favor tente novamente!')
        sleep(1)
        menu()

if __name__=='__main__':
    menu()


