def cabecalho(mensagem):
    print('-' * (len(mensagem) + 4))
    print(mensagem.center((len(mensagem) + 4)))
    print('-' * (len(mensagem) + 4))


def menu(*opcoes):
    for item in opcoes:
        print(item)