class Functions:
    def adicionar(lista):
        print("digite o nome do produto")
        nome = input()
        return lista.append(nome)
    def listar(lista):
        print(lista)
    def apagar(lista, nomeProduto):
        lista.remove(nomeProduto)
    def modificar(lista, nome, newProduto):
        indice = lista.index(nome)
        lista[indice] = newProduto
class Mercado:
    produtos = []
    while True:
        print("hello")
        print("O que deseja fazer?")
        print("1-Adicionar um produto \n2-listar produtos \n3-apagar\n4-modifica\n5-sair")
        desc = input()
        if desc == "1":
            Functions.adicionar(produtos)
        elif desc == "2":
            Functions.listar(produtos)
        elif desc == "3":
            print("qua produtos deseja apagar:")
            Functions.listar(produtos)
            produto = input()
            Functions.apagar(produtos, produto)
        elif desc == "4":
            print("qua produtos deseja modificar:")
            Functions.listar(produtos)
            produto = input()
            print("qual o novo nome para o produto?")
            newProduto = input()
            Functions.modificar(produtos,produto,newProduto)
        elif desc == "5":
            break