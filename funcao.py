"""
Mycode Package
----------------
Fala oi

"""
def sayHello(msg):
    """
    :param msg: -Messagem que será mostrada
    :return: str
    """
    return print(f'{msg}')


def gritar(funcao):
    """
    :param funcao: func
    :return: letras grandes
    """
    def aumentar(*args, **kwargs):
        return  funcao(*args, *kwargs).upper()
    return aumentar
