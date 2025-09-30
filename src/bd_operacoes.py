from pathlib import Path

def HistoricoOperacoes(arq, operacao):
    if not Path(f'{arq}.txt').exists():
        print("Excelente, agora digite aqui o nome que gostaria de dar ao arquivo onde vão constar o histórico de operações")
        arq = str(input())
        with open(f'{arq}.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write(f'{operacao}\n')
            arquivo.close()
        
    else:
        with open(f'{arq}.txt', 'a+', encoding='utf-8') as arquivo:
            arquivo.write(f'{operacao}\n')
            arquivo.close()
        print("Arquivo atualizado")
    
    return arquivo    
