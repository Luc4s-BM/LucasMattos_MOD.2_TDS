import os

eventos = []

def validar_entradaINT(entrada):
    while True:
        try:
            return int(entrada)
        except ValueError:
            entrada = input("Digite um valor válido!: ")

def cadastrar_eventos():
    while True:
        evento = input("Digite o nome do evento: ").strip().lower()
        if not evento:
            print("O nome do evento não pode ser vazio. Tente novamente.")
            continue
        capacidade_de_pessoas = None
        while capacidade_de_pessoas is None or capacidade_de_pessoas <= 0:
            capacidade_de_pessoas = validar_entradaINT(input(f'Digite a quantidade máxima de pessoas para o evento "{evento.capitalize()}": '))
            if capacidade_de_pessoas <= 0:
                print("A capacidade precisa ser um número inteiro positivo. Tente novamente.")
        if any(i["nome"] == evento for i in eventos):
            print(f'O evento "{evento.capitalize()}" já está cadastrado.')
            return
            
        evento_cadastrado = {
            "nome": evento, 
            "capacidade": capacidade_de_pessoas, 
            "alunos": 0
        }
    
        eventos.append(evento_cadastrado)
        print(f'Evento "{evento.capitalize()}" cadastrado com sucesso, com a capacidade máxima de {capacidade_de_pessoas} pessoas!')
        break

def exibir_lista_de_eventos():
    if not eventos:
        print("Não há eventos cadastrados.")
    else:
        print("\nLista de eventos cadastrados:")
        for i, evento in enumerate(eventos, start=1):
            print(f'{i}. Evento: {evento["nome"].capitalize()} - Capacidade: {evento["capacidade"]} pessoas - Vagas restantes: {evento["capacidade"] - evento["alunos"]} vagas')

def buscar_evento(nome_evento):
    for evento in eventos:
        if evento["nome"] == nome_evento:
            return evento
    return None

def add_alunos_interessados_no_evento():
    if not eventos:
        print("Não há eventos para adicionar alunos.")
        return
    while True:
        exibir_lista_de_eventos()
        escolher_evento_cadastrado = input("Digite o nome do evento para adicionar os alunos interessados: ").strip().lower()
        evento_encontrado = buscar_evento(escolher_evento_cadastrado)
        if evento_encontrado is not None:
            quantidade_de_alunos = None
            while quantidade_de_alunos is None:
                quantidade_de_alunos = validar_entradaINT(input(f'Digite quantos alunos participarão do evento "{escolher_evento_cadastrado.capitalize()}": '))
                if evento_encontrado["alunos"] + quantidade_de_alunos > evento_encontrado["capacidade"]:
                    print("A quantidade de alunos excede a capacidade do evento! Tente novamente.")
                    quantidade_de_alunos = None
            evento_encontrado["alunos"] += quantidade_de_alunos
            print(f'Alunos adicionados com sucesso! Total de alunos no evento "{evento_encontrado["nome"].capitalize()}": {evento_encontrado["alunos"]}')
            break
        else:
            print("Digite um evento válido!")

def excluir_evento_cadastrado():
    if not eventos:
        print("Não há eventos para excluir.")
        return
    exibir_lista_de_eventos()
    evento = input("Digite o nome do evento para excluir: ").strip().lower()
    evento_encontrado = buscar_evento(evento)
    if evento_encontrado:
        if evento_encontrado["alunos"] > 0:
            print(f"O evento '{evento.capitalize()}' ainda tem alunos cadastrados e não pode ser excluído!")
        else:
            eventos.remove(evento_encontrado)
            print(f'O evento "{evento.capitalize()}" foi excluído com sucesso!')
    else:
        print("Evento não encontrado!")

def excluir_alunos_cadastrados_e_atualizar():
    if not eventos:
        print("Não há eventos para excluir alunos.")
        return
    exibir_lista_de_eventos()
    escolha_evento_para_excluir_alunos = input("Digite o nome do evento para excluir os alunos: ").strip().lower()
    evento_encontrado = buscar_evento(escolha_evento_para_excluir_alunos)
    if evento_encontrado:
        if evento_encontrado["alunos"] > 0:
            print(f'{evento_encontrado["alunos"]} alunos removidos do evento "{escolha_evento_para_excluir_alunos.capitalize()}" com sucesso!')
            evento_encontrado["alunos"] = 0
        else:
            print("Esse evento não contém participantes!")
    else:
        print("Evento não encontrado!")

def resumo_da_participacao_dos_alunos():
    if not eventos:
        print("Não houve eventos cadastrados.")
    else:
        print("\n--- RESUMO SNCT 2024 ---")
        for i, evento in enumerate(eventos, start=1):
            print(f'{i}. Evento: {evento["nome"].capitalize()} - Participantes: {evento["alunos"]} alunos')

def imprimir_resumo_scnt():
    with open("exercicios_vscode/Resultado da SCNT 2024.txt", "w") as arquivo:
        if not eventos:
            arquivo.write("Não houve eventos cadastrados.\n")
        else:
            arquivo.write("--- RESUMO SNCT 2024 ---\n")
            for evento in eventos:
                arquivo.write(f'Evento: {evento["nome"].capitalize()} - Participantes: {evento["alunos"]} alunos\n')
                
def excluir_impressão():
    escolha_de_tipo_de_arquivo = input("""Qual o tipo de arquivo que você quer excluir?
1 - .txt
2 - .pdf
3 - .doc
4 - .html
Digite sua escolha: """)
    if escolha_de_tipo_de_arquivo == "1" or escolha_de_tipo_de_arquivo == "txt" or escolha_de_tipo_de_arquivo == ".txt":
        os.remove("exercicios_vscode/Resultado da SCNT 2024.txt")
        print("Arquivo excluído com sucesso!")
    elif escolha_de_tipo_de_arquivo == "2" or escolha_de_tipo_de_arquivo == "pdf" or escolha_de_tipo_de_arquivo == ".pdf":
        os.remove("exercicios_vscode/Resultado da SCNT 2024.pdf")
        print("Arquivo excluído com sucesso!")
    elif escolha_de_tipo_de_arquivo == "3" or escolha_de_tipo_de_arquivo == "doc" or escolha_de_tipo_de_arquivo == ".doc":
        os.remove("exercicios_vscode/Resultado da SCNT 2024.doc")
        print("Arquivo excluído com sucesso!")
    elif escolha_de_tipo_de_arquivo == "4" or escolha_de_tipo_de_arquivo == "html" or escolha_de_tipo_de_arquivo == ".html":
        os.remove("exercicios_vscode/Resultado da SCNT 2024.html")
        print("Arquivo excluído om sucesso!")

def menu_de_opcoes():    
    while True:
        escolha = input("""--- SNCT 2024 ---
1 - Cadastrar evento.
2 - Excluir evento cadastrado.
3 - Cadastrar alunos em um evento.
4 - Excluir alunos cadastrados no evento.
5 - Exibir lista de eventos e alunos cadastrados.
6 - Excluir impresões doevento anteriores.
7 - Digite "Sair" para encerrar e imprimir resumo dos eventos.
Digite sua opção: """).strip().lower()
        
        if escolha == "1":
            cadastrar_eventos()
            print("="*70)
            
        elif escolha == "2":
            excluir_evento_cadastrado()
            print("="*70)

        elif escolha == "3":
            add_alunos_interessados_no_evento()
            print("="*70)

        elif escolha == "4":
            excluir_alunos_cadastrados_e_atualizar()
            print("="*70)

        elif escolha == "5":
            exibir_lista_de_eventos()
            print("="*70)

        elif escolha == "6":
            excluir_impressão()
            
        elif escolha == "7" or escolha == "sair":
            resumo_da_participacao_dos_alunos()
            imprimir_resumo_scnt()
            print('Impressão passada para o arquivo: "Resultado da SCNT 2024".')
            print("### FIM DO PROGRAMA ###")
            break
        else: 
            print(f'Não há opção "{escolha}" no menu.')
            print("="*70)

menu_de_opcoes()