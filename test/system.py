def calcular(v1, simbolo, v2):
    if simbolo == '+':
        return v1 + v2
    elif simbolo == '-':
        return v1 - v2
    elif simbolo == 'X':
        return v1 * v2
    elif simbolo == '/':
        return v1 / v2
    else:
        print('Simbolo inválido!')
