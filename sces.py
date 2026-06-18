## Definindo as variáveis

Matriz_Produtos = [
    []
]

## Início do programa

print("\n------ Sistema de Controle de Estoque Simplificado (SCES) -----")


## Cadastrando novo produto

def Cadastrar_Produto():
    global Matriz_Produtos
    id_Produto = input("-- Digite o id do produto (numérico): ")
    nome_produto = input("-- Digite o nome do produto (texto): ")
    quanti_produto = input("-- Digite a quantidade do produto (numérico): ")
    local_produto = input("-- Digite a localização do produto (ex:'A-01-03'): ")

# Lista com os dados do produto a ser cadastrado

    Novo_Produto = [id_Produto, nome_produto, int(quanti_produto), local_produto]
    Matriz_Produtos.append(Novo_Produto)
    print("-- Produto cadastrado com sucesso! ✅")

## Listando os produtos cadastrados

def Listar_Produtos():
    global Matriz_Produtos
    print(f"-- Listando todos os produtos cadastrados: {Matriz_Produtos}:")
    for produto in Matriz_Produtos:
        print(f"ID: {produto[0]} | Nome: {produto[1]} | Quantidade: {produto[2]} | Localização: {produto[3]}")

## Buscar produto por ID

def Buscar_ID_Produto():
    global Matriz_Produtos
    id_Produto = input("-- Digite o ID do produto que deseja procurar: ")
    
    for produto in Matriz_Produtos:
        if produto[0] == id_Produto:
            print(f"id do produto: {id_Produto}")
            print(f"Nome: {produto[1]} | Qtd: {produto[2]} | Local: {produto[3]}")
            
        
    print("-- Produto não encontrado! ❌")

 
