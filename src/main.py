from soma import Soma

def main():
    metds = ['Soma', 'Subtração', 'Divisão', 'Multiplicação', 'Raiz quadrada', 'Potência']
    titulo = 'CALCULADORA CLI'
    print("=-"*20)
    print(f'{titulo:^40}')
    print("=-"*20)
    print("O que vamos fazer?")

    for num, metd in enumerate(metds):
        print(f'[{num + 1}]{metd}')
    op = int(input("Digite aqui sua opção: "))
    
    match op:
        case 1:
            resultado = Soma()
            print(f"O resultado da soma é: {resultado}")
        case 2:
            ...
        case 3:
            ...
        case 4:
            ...
        case 5:
            ...
        case 6:
            ...

if __name__ == "__main__":
    main()
