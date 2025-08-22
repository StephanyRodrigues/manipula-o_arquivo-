def processar_arquivo():
    # Abre o arquivo de entrada para leitura
    with open("entrada.txt", "r", encoding="utf-8") as arquivo_entrada:
        linhas = arquivo_entrada.readlines()
    
    linhas_processadas = []
    
    for linha in linhas:
        # Verifica se a linha contém a palavra "ignorar"
        if "ignorar" in linha.lower():
            continue  # Pula essa linha
        
        # Substitui "problema" por "desafio"
        linha_modificada = linha.replace("problema", "desafio")
        
        # Também substitui "Problema" com P maiúsculo (caso apareça)
        linha_modificada = linha_modificada.replace("Problema", "Desafio")
        
        linhas_processadas.append(linha_modificada)
    
    # Grava as linhas processadas em um novo arquivo
    with open("saida.txt", "w", encoding="utf-8") as arquivo_saida:
        arquivo_saida.writelines(linhas_processadas)


# Executa a função
processar_arquivo()
