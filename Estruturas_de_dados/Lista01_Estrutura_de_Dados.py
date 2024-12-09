#1
dias_da_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabádo", "Domingo")
meses_do_ano = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
estacoes_do_ano =  ("Verão", "Outono"," Inverno", "Primavera")
data = (dias_da_semana, meses_do_ano, estacoes_do_ano)
def main(tupla):
    print("Dias da Semana: ", tupla[0])
    print("Meses do Ano: ", tupla[1])
    print("Estações do Ano: ", tupla[2])
print("Data Tipo Tupla:")
main(data)
print("="*50)

#2
dias_da_semana2 = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabádo", "Domingo"]
meses_do_ano2 = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
estacoes_do_ano2 = ["Verão", "Outono"," Inverno", "Primavera"]
data2 = [dias_da_semana2, meses_do_ano2, estacoes_do_ano2]
def main2(lista):
    print("Dias da Semana: ", lista[0])
    print("Meses do Ano: ", lista[1])
    print("Estações do Ano: ", lista[2])
print("Data Tipo Lista:")   
main2(data2)
print("="*50)

#3
dias_da_semana3 = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabádo", "Domingo"]
meses_do_ano3 = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
estacoes_do_ano3 = ["Verão", "Outono","Inverno", "Primavera"]

def imprimir(lista2):
    print("Tamanho: ", len(lista2))
    print("Dados: ", lista2[0], lista2[2], lista2[-1])
    
imprimir(dias_da_semana3)
imprimir(meses_do_ano3)
imprimir(estacoes_do_ano3)
print("="*50)

#4
lista4 = []

def lista_de_compras():
    print("Crie sua lista de compras (máximo 15 itens):")
    numero_do_item4 = 1
    while numero_do_item4 <= 15: 
        item4 = input(f"-> Digite o {numero_do_item4}º item da sua lista de compras: ").strip().title()
        lista4.append(item4)
        numero_do_item4 += 1
    exibir_lista()
lista_de_compras()
print("="*50)
#5
lista4 = []

def exibir_lista():
    print("Aqui está sua lista de compras:")
    for i, item in enumerate(lista4, start=1):
        print(f"{i}º - {item.capitalize()}")

def incluir_item():
    while True:
        if len(lista4) >= 15:
            print("Sua lista já está no limite de 15 itens! Não é possível adicionar mais.")
            break
        novo_item = input("Digite o item que deseja incluir (ou digite 'PRONTO' para finalizar): ").strip().title()
        if novo_item.lower() == "pronto":
            break
        lista4.append(novo_item)
    exibir_lista()

def remover_item():
    exibir_lista()
    item_para_remover = input("Digite o nome do item que deseja remover: ").strip().title()
    if item_para_remover in lista4:
        lista4.remove(item_para_remover)
        print(f"O item '{item_para_remover}' foi removido com sucesso!")
    else:
        print("Este item não está na lista.")
    exibir_lista()

def atualizar_item():
    exibir_lista()
    item_para_atualizar = input("Digite o nome do item que deseja atualizar: ").strip().title()
    if item_para_atualizar in lista4:
        novo_valor = input(f"Digite o novo valor para o item '{item_para_atualizar}': ").strip().title()
        indice = lista4.index(item_para_atualizar)
        lista4[indice] = novo_valor
        print(f"O item '{item_para_atualizar}' foi atualizado para '{novo_valor}'.")
    else:
        print("Este item não está na lista.")
    exibir_lista()

def menu():
    while True:
        print("\nEscolha uma das opções:")
        print("1 - Incluir um novo item")
        print("2 - Remover um item")
        print("3 - Atualizar um item existente")
        print("4 - Exibir lista")
        print("5 - Encerrar o programa")
        opcao = input("Digite o número da opção desejada: ").strip()
        if opcao == "1":
            incluir_item()
        elif opcao == "2":
            remover_item()
        elif opcao == "3":
            atualizar_item()
        elif opcao == "4":
            exibir_lista()
        elif opcao == "5":
            print("Programa encerrado. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()
print("="*50)

#6
linguagens_ocultas = ["C", "C++", "JavaScript", "Java", "Lua", "Python"]

def adivinhar_linguagem_oculta():
    print('Adivinhe as linguagens que constam na lista oculta! (Quando quiser encerrar digite "SAIR").')
    while True:
        tentativa = input("Sua tentativa: ").strip().title()
        if tentativa in linguagens_ocultas:
            print(f"A linguagem {tentativa} consta na lista!")
        elif tentativa.lower() == "sair":
            print("--- Programa encerrado ---")
            break
        else:
            print(f"A linguagem {tentativa} não consta na lista!")
adivinhar_linguagem_oculta()
print("="*50)

#7
lista_de_medicos = ["Alice Monteiro", "Lucas Almeida", "Beatriz Carvalho", "Gabriel Nogueira", "Marina Fernandes", "Rafael Costa", "Sofia Martins"]
print("Olá, com qual médico você deseja marcar uma consulta?")
for i, medico in enumerate(lista_de_medicos, start=1):  
    print(f"{i}. {medico}") 
def escolher_medico():
    while True:
        escolha = input("Digite o nome do médico que vocâ deseja marcar sua consulta (Digite o número respectivos ao medico desejado): ")
        if escolha == "1":
            print(f"Consulta com o(a) médico {lista_de_medicos[0]} marcada.")
            break
        elif escolha == "2":
            print(f"Consulta com o(a) médico {lista_de_medicos[1]} marcada.")
            break
        elif escolha == "3":
            print(f"Consulta com o(a) médico {lista_de_medicos[2]} marcada.")
            break
        elif escolha == "4":
            print(f"Consulta com o(a) médico {lista_de_medicos[3]} marcada.")
            break
        elif escolha == "5":        
            print(f"Consulta com o(a) médico {lista_de_medicos[4]} marcada.")
            break
        elif escolha == "6":
            print(f"Consulta com o(a) médico {lista_de_medicos[5]} marcada.")
            break
        else:
            print("Digite uma opção válida!")
escolher_medico()






