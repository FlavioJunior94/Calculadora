def binario (x):
    return bin(x)[2:]

def hexadecimal (x):
    return hex(x)[2:]

def if_binario(x):
    try:
        int(x,2)
        return True
    except:
        return False

def if_hexadecimal(x):
    try:
        int(x,16)
        return True
    except:
        return False

def decimal(x):
    decimal_num=int(x,2)
    return decimal_num