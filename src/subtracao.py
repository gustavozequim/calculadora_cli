from datetime import datetime


def Subtracao():
    a = int(input('Digite o primeiro numero: '))
    b = int(input('Digite o segundo numero: '))
    return f"{a} - {b} = {a - b} - {datetime.now().__format__('%d/%m/%Y - %H:%M:%S')}"