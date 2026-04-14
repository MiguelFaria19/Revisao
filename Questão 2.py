dados = []

def adicionar_livro(dados_livros):
    titulo = input("Titulo: ")
    autor = input("autor: ")
    
    while True:
        try:
            ano = int(input("Ano: "))
            paginas = int(input("Paginas: "))
            if ano or paginas > 0:
                break
        except:
            print("Ano/Paginas Invalidas")
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "paginas": paginas
    }
    dados_livros.append(livro)

def listar_livros(dados_livros):
    while True:
        try:
            for i in dados_livros:
                print(f"{i['titulo']}")
        except:
            print("N tem livros cadastrados")
        break
    else:
        print("Erro")

def ordenar_livros(dados_livros):
    "x"

def salvar_arquivo(dados_livros):
    with open("Biblioteca.txt", "w") as arquivo:
        for i in dados_livros:
            linha = f"{i['titulo']}, {i['autor']}, {i['ano']}, {i['paginas']}.\n"
            arquivo.write(linha)
    print("Dados salvos!")

def carregar_livros(dados_livros):
        with open("biblioteca.txt", "r") as f:
            for linha in f:
                titulo, autor, ano, paginas = linha.strip().split(",")
                dados.append({
                    "titulo": titulo,
                    "autor": autor,
                    "ano": int(ano),
                    "paginas": int(paginas)
                })
        print("Dados carregados!")

while True:
    print("\n1-Adicionar  2-Listar  3-Ordenar  4-Salvar  5-Carregar  6-Sair")
    op = input("Escolha: ")
    
    if op == "1":
        adicionar_livro(dados)
    elif op == "2":
        listar_livros(dados)
    elif op == "3":
        ordenar_livros(dados)
    elif op == "4":
        salvar_arquivo(dados)
    elif op == "5":
        carregar_livros(dados)
    elif op == "6":
        s = input("Deseja salvar antes de sair? (S/N): ").upper()
        if s == "S":
            carregar_livros(dados)
        break
    else:
        print("Opção inválida.")