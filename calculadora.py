from models import operacoes_simples, conversor_base, gerador_senha, cotacao
from time import sleep
def menu():
    print("""
        =================================
        ==========CALCULADORA ==========
        ================================
        =======ESCOLHA A OPERAÇÃO=======
        ================================
        1 - OPERAÇÕES SIMPLES( +-*/ )
        2 - CONVERSOR BASE
        3 - CONVERSOR DE MOEDA
        4 - BHASKARA
        5 - GERADOR DE SENHAS
        6 - FECHAR CALCULADORA 
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
    elif op==2:
        conversor_base.menu_base()
    elif op==3:
        #cotacao.cotar()
        print(f"""
        --COTACAO ATUAL (em Reais R$)---
        | Dolar:{float(cotacao.cotar()[0]):.2f}
        | Euro:{float(cotacao.cotar()[1]):.2f}
        | BTC:{float(cotacao.cotar()[2]):.2f}
        --------------------------------
        """)
        sleep(1)
        while True:
            try:
                valor = float(input('Insira o valor em reais (R$): '))
                break
            except:
                print('dado invalido! tente novamente.')

        print(f"""
        seu valor em:
        Dolar: US$ {valor/float(cotacao.cotar()[0]):.2f}
        Euro: € {valor/float(cotacao.cotar()[1]):.2f}
        Bitcoin: ₿ {valor/float(cotacao.cotar()[2]):.2f}
        
        """)
        sleep(3)
        menu()
    elif op==4:
        pass
    elif op==6:
        print('\n Volte sempre ! :)')
        exit()
    elif op==5:
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


