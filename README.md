# 🌟 Sistema de Controle de Estoque Simplificado (SCES)

Sistema de controle de estoque simplificado e interativo via terminal, feito para quem precisa gerenciar inventários sem complicação. Com ele, você cadastra, lista, busca e atualiza a quantidade de produtos instantaneamente em uma interface leve e direta. 

# ❔ Funcionalidades

## Menu interativo: 
* O menu interativo fornece opções como: Opção 1 - Cadastrar produtos, Opção 2- Listar produtos cadastrados, Opção 3- Buscar produtos pelo ID, Opção 4- Atualizar estoque e Opção 5- Sair do programa.

### Opção 1 - Cadastrar produtos:
* A opção 1 mostrará opções como: 
- Digite o ID do produto (numérico)
- Digite o nome do produto (texto)
- Digite a quantidade do produto (numérico) 
- Digite a localização do produto (ex:`A-01-03`)

⚠️ *Regra:* Caso digite um número negativo, o sistema recusa o cadastro e retorna ao menu principal


### Opção 2 - Listar produtos cadastrados:
* Exibe todos os produtos armazenados na memória do sistema formatados em uma única linha para facilitar a leitura rápida


### Opção 3 - Buscar produtos pelo ID:
* Filtra e exibe detalhadamente os dados apenas do produto correspondente ao ID informado
* Retorna um aviso caso o ID não seja encontrado na base de dados

### Opção 4 - Atualizar estoque
* A opção 4 irá solicitar o ID do produto e exibir:
-  Digite o ID do produto que deseja atualizar
- Insira a nova quantidade numérica


⚠️ *Remoção Automática:* Se o novo valor informado for **menor ou igual a zero (≤ 0)**, o produto é deletado automaticamente do estoque


### Opção 5 - Sair do programa:
* Finaliza por completo a execução do sistema 


# 🛠️ Tecnologias Utilizadas

*Linguagem principal* - Python 3

*Estrutura de dados* - Matrizes / Listas




