from datetime import datetime

def Multiplicacao():
    try:
        a = int(input('Digite o primeiro numero: '))
        b = int(input('Digite o segundo numero: '))
        return f"{a} x {b} = {a*b} - {datetime.now().__format__('%d/%m/%Y - %H:%M:%S')}"
    except Exception as e:
        return print(f"Houve um erro ao multiplicar:\n {e}")
