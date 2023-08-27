def metade(num = 0, formato = False):
    """_summary_

    Args:
        num (int, optional): _description_. Defaults to 0.
        formato (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    res = num / 2
    return res if formato is False else moeda(res)


def dobro(num = 0, formato = False):
    """_summary_

    Args:
        num (int, optional): _description_. Defaults to 0.
        formato (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    res = num * 2
    return res if formato is False else moeda(res)


def aumentar(num = 0, x = 0, formato = False):
    """_summary_

    Args:
        num (int, optional): _description_. Defaults to 0.
        x (int, optional): _description_. Defaults to 0.
        formato (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    res = num * (1 + (x / 100))
    return res  if formato is False else moeda(res)


def diminuir(num = 0, x = 0, formato = False):
    """_summary_

    Args:
        num (int, optional): _description_. Defaults to 0.
        x (int, optional): _description_. Defaults to 0.
        formato (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    res = num * (1 - (x / 100))
    return res if formato is False else moeda(res)


def moeda(x, moeda = 'R$'):
    """_summary_

    Args:
        x (_type_): _description_
        moeda (str, optional): _description_. Defaults to 'R$'.

    Returns:
        _type_: _description_
    """
    return f'{moeda}{x:.2f}'.replace('.', ',')


def resumo(preco = 0, taxaa = 10, taxar = 5):
    print('-' * 33)
    print('RESUMO DO VALOR'.center(33))
    print('-' * 33)
    print(f'Preço analisado: \t{moeda(preco)}')
    print('-' * 33)
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-' * 33)