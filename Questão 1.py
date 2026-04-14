#1
dados = []

def adicionar_aluno(dados_aluno):
    nome = input("Nome do aluno: ")
    
    notas = []
    a = int(input("Quantas avaliações ele fez? (de 1 a 5): "))
    if a > 0 and a < 5:
        for i in range(a):
            x = float(input(f"Nota: "))
            notas.append(x)
    else:
        print("Quantidade invalida")
        return

    media = sum(notas)/len(notas)

    dado = {
        "nome": nome,
        "notas": notas,
        "media": media
    }
    dados_aluno.append(dado)

def ordenar_alunos(dados_aluno):
    dados.sort(key=lambda x: x["media"], reverse=True)

def Salvar_em_arquivo(dados_aluno):
    with open("alunos.txt", "w") as arquivo:
        for i in dados_aluno:
            linha = f"{i['nome']} - {i['media']}\n"
            arquivo.write(linha)

    print("Dados salvos em alunos.txt com sucesso!")

def mostrar_alunos(dados_aluno):
    print("Alunos ordenados por média:")
    for aluno in dados:
        print(f"{aluno['nome']} - Média: {aluno['media']}")

while True:

    print("1 - Adicionar aluno")
    print("2 - Finalizar e mostrar resultado")
    
    op = input("Escolha: ")
    if op == "1":
        adicionar_aluno(dados)
    
    elif op == "2":
        if len(dados) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            ordenar_alunos(dados)
            mostrar_alunos(dados)
            Salvar_em_arquivo(dados)
            break
    else:
        print("Opção inválida.")