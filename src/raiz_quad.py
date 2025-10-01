from datetime import datetime


def RaizQuadrada():
    try:
        a = int(input('Digite um numero: '))
        return f"Raiz quadradada de {a} = {a ** 0.5} - {datetime.now().__format__('%d/%m/%Y - %H:%M:%S')}"
    except Exception as e:
        return print(f"Houve um erro ao calcular a raiz quadrada:\n{e}")
