from soma import Soma
from multiplicacao import Multiplicacao
from raiz_quad import RaizQuadrada
from potencia import Potencia
from subtracao import Subtracao
from divisao import Divisao

def main():
    metds = ['Soma', 'Subtração', 'Divisão', 'Multiplicação', 'Raiz quadrada', 'Potência']
    titulo = 'CALCULADORA CLI'
    print("=-"*20)
    print(f'{titulo:^40}')
    print("=-"*20)
    print("O que vamos fazer?")
    print("=-"*20)
    for num, metd in enumerate(metds):
        print(f'[{num + 1}]{metd}')
    print("=-"*20)
    op = int(input("Digite aqui sua opção: "))
    print("=-"*20)
    match op:
        case 1:
            resultado = Soma()
            print("=-"*20)
            print(f"O resultado da soma é: {resultado}")
        case 2:
            resultado = Subtracao()
            print("=-"*20)
            print(f'O resultado da subtração é: {resultado}')
        case 3:
            resultado = Divisao()
            print("=-"*20)
            print(f"O resultado da divisão é: {resultado}")
        case 4:
            resultado = Multiplicacao()
            print("=-"*20)
            print(f"O resultado da multiplicação é: {resultado}")
        case 5:
            resultado = RaizQuadrada()
            print("=-"*20)
            print(f"O resultado da raiz quadrada é: {resultado}")
        case 6:
            resultado = Potencia()
            print("=-"*20)
            print(f"O resultado da potência é: {resultado}")

if __name__ == "__main__":
    main()
