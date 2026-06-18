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



