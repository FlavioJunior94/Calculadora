def bhaskara(a,b,c):
    n1=4*a*c
    n2=(b)**2
    n3= 2*a
    n4=(n2)-(n1)
    raiz=(n4**(1/2))
    bb= -1 *b
    x1=(bb+raiz)/n3
    x2=(bb-raiz)/n3
    return print(f'x1= {x1:.2f} e x2= {x2 :.2f}')

"""
n1 = 4*va*vc
    n2 = (vb)**2
    n3 = 2 * va
    n4 = (n2) - (n1)
    raiz = (n4 ** (1 / 2))
    bb = -1 * vb
    x1 = (bb + raiz) / n3
    x2 = (bb - raiz) / n3
    texto_final["text"]=f'x1= {x1:.2f} e x2= {x2 :.2f}'

"""

