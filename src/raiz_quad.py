from datetime import datetime


def RaizQuadrada():
    a = int(input('Digite um numero: '))
    return f"Raiz quadradada de {a} = {a ** 0.5} - {datetime.now().__format__('%d/%m/%Y - %H:%M:%S')}"
