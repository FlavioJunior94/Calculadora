import string
import numpy as np
def gerador_senha(tam_senha):
    caracter= string.punctuation + string.ascii_letters + string.digits
    senha=""

    for i in list(np.random.choice(list(caracter),tam_senha)):
        senha+=i
    return print(senha)