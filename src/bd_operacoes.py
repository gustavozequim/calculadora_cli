from pathlib import Path

def HistoricoOperacoes(operacao):
    try:
        print("Excelente, agora digite aqui o nome do arquivo com histórico de operações")
        arq = str(input())
        if not Path(f'{arq}.txt').exists():
            print("Ops, vi que esse arquivo não existe, mas vamos criá-lo")
            with open(f'{arq}.txt', 'w', encoding='utf-8') as arquivo:
                arquivo.write(f'{operacao}\n')
                arquivo.close()
            print("Tudo certo!")

        else:
            with open(f'{arq}.txt', 'a+', encoding='utf-8') as arquivo:
                arquivo.write(f'{operacao}\n')
                arquivo.close()
            print("Arquivo atualizado com sucesso!")

        return arquivo    
    except Exception as e:
        return print(f"Ocorreu um erro ao lidar com o arquivo de histórico:\n{e}")