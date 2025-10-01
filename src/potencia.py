from datetime import datetime


def Potencia():
    try:
        a = int(input("Digite o numero para calcular a potencia: "))
        return f"{a}^2 = {a**2} - {datetime.now().__format__('%d/%m/%Y - %H:%M:%S')}"
    except Exception as e:
        return print(f"Houve um erro ao calcular a potencia:\n{e}")
