## Definindo as variáveis

Matriz_Produtos = [ 
    [1, "Chocolate", 4, "C-06-27"],
    [2, "Sorvete", 100, "S-07-28"],
    [6, "Bolacha Recheada", 15, "B-03-30"],
    [8, "Paçoca", 50, "P-09-40"]
    ]

id_Produto = 0 

## Início do programa

print("\n------ Sistema de Controle de Estoque Simplificado (SCES) -----")


## Cadastrando novo produto

def Cadastrar_Produto():
    global Matriz_Produtos
    print("\n--- CADASTRAR NOVO PRODUTO ---")
    id_Produto = input("-- Digite o id do produto (numérico): ")
    nome_produto = input("-- Digite o nome do produto (texto): ")

    quanti_produto = int(input("-- Digite a quantidade do produto (numérico): "))

    if quanti_produto < 0:
        print("\nNúmeros negativos são proibidos! ❌")
        Travar_Menu()
        return
        
    local_produto = input("-- Digite a localização do produto (ex:'A-01-03'): ")


## Listando os dados do produto a ser cadastrado

    Novo_Produto = [int(id_Produto), nome_produto, int(quanti_produto), local_produto]
    Matriz_Produtos.append(Novo_Produto)
    print("\n-- Produto cadastrado com sucesso! ✅")


## Listando todos os produtos cadastrados

def Listar_Produtos():
    global Matriz_Produtos
    print("\n--- LISTAR PRODUTO(S) ---")
    print(f"\n-- Listando todos os produtos cadastrados:")
    for linha in Matriz_Produtos: ## Lista a linha com todas as informações do produto 
        print(linha)
        
    Travar_Menu()


## Buscando produto pelo ID

def Buscar_ID_Produto():
    print("\n--- BUSCAR PRODUTO PELO ID ---")
    global Matriz_Produtos
    id_Produto = int(input("\n-- Digite o ID do produto que deseja procurar: "))

    for produto in Matriz_Produtos:
        if produto[0] == id_Produto:
            print(f"\nID do produto: {id_Produto}")
            print(f"\nNome: {produto[1]} | Qtd: {produto[2]} | Local: {produto[3]}") ## Localiza 
            break
    
    else:
         print("\n-- Produto inexistente! ❌ Volte para Menu Interativo e selecione a opção 1 !")
        
    Travar_Menu()


## Atualizando estoque dos produtos

def Atualizar_Estoque():
    print("\n--- ATUALIZAR ESTOQUE ---")
    global Matriz_Produtos
    Produto_Procurado = -1
    Quanti_Estoque = 0

    id_Produto = int(input("\n-- Digite o ID do produto que deseja atualizar (numérico): "))

    ## Verifica se encontrou o produto

    for i in range(len(Matriz_Produtos)):
        if(Matriz_Produtos[i][0] == id_Produto):
            Produto_Procurado = i  ## Essa função confere se o produto está cadastrado

    ## Se o produto não estiver cadastrado:
    if Produto_Procurado == -1:
         print("-- Produto não cadastrado! ❌") 

    ## Se o produto estiver cadastrado:
    else:
        Nova_quanti = int(input("-- Insira a nova quantidade do produto (numérico): "))

        if Nova_quanti <= 0:
            Matriz_Produtos.pop(Produto_Procurado)
            print("-- O produto foi removido do estoque!")

        else:
            Matriz_Produtos[Produto_Procurado][2] = Nova_quanti
            print(f"Quantidade do produto ID: {id_Produto} redefinido para: {Nova_quanti} !")


    Travar_Menu()


## Travando o menu interativo

def Travar_Menu():
    input("\nPressione <ENTER> para continuar...")


## Rodando o menu interativo do programa

while True: 
    print("\n--- Bem-vindo(a) ao SCES!")
    print(f"\n| 1. Cadastrar Produto | 2. Listar Todos os Produtos | 3. Buscar Produto por ID | 4. Atualizar Estoque | 5. Sair do Programa |")
    opcao = input("\n-- Selecione a opção desejada: ")
    if (opcao == "1"):
        Cadastrar_Produto()
    elif (opcao == "2"):
        Listar_Produtos()
    elif (opcao == "3"):
        Buscar_ID_Produto()      
    elif (opcao == "4"):    
        Atualizar_Estoque()
    else:    
        print("\n Saindo do programa...")
        break
