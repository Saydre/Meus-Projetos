class Bandagem:
    def __init__(self, cor, tamanho, quantidade):
        self.cor = cor
        self.tamanho = tamanho
        self.quantidade = quantidade

class Estoque:
    def __init__(self):
        self.estoque = []

    def adicionar_bandagem(self, cor, tamanho, quantidade):
        for bandagem in self.estoque:
            if bandagem.cor == cor and bandagem.tamanho == tamanho:
                bandagem.quantidade += quantidade
                print(f"Quantidade de {cor}, {tamanho} atualizada para {bandagem.quantidade}.")
                return
        nova_bandagem = Bandagem(cor, tamanho, quantidade)
        self.estoque.append(nova_bandagem)
        print(f"Bandagem {cor}, {tamanho} adicionada com quantidade {quantidade}.")

    def remover_bandagem(self, cor, tamanho):
        self.estoque = [b for b in self.estoque if not (b.cor == cor and b.tamanho == tamanho)]
        print(f"Bandagem {cor}, {tamanho} removida do estoque.")

    def alterar_quantidade(self, index, nova_quantidade):
        if 0 <= index < len(self.estoque):
            bandagem = self.estoque[index]
            bandagem.quantidade = nova_quantidade
            print(f"Quantidade de {bandagem.cor}, {bandagem.tamanho} alterada para {nova_quantidade}.")
        else:
            print("Índice inválido. Não foi possível alterar a quantidade.")

    def consultar_estoque(self):
        if not self.estoque:
            print("Nenhum item no estoque.")
            return
        for i, bandagem in enumerate(self.estoque):
            print(f"{i}. Cor: {bandagem.cor}, Tamanho: {bandagem.tamanho}, Quantidade: {bandagem.quantidade}")

# Função principal com menu interativo
def menu():
    estoque = Estoque()
    
    while True:
        print("\nMenu de Opções:")
        print("1. Adicionar bandagem")
        print("2. Remover bandagem")
        print("3. Alterar quantidade de uma bandagem")
        print("4. Consultar estoque")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            cor = input("Digite a cor da bandagem: ")
            tamanho = input("Digite o tamanho da bandagem: ")
            quantidade = int(input("Digite a quantidade de bandagens: "))
            estoque.adicionar_bandagem(cor, tamanho, quantidade)
        
        elif escolha == "2":
            cor = input("Digite a cor da bandagem que deseja remover: ")
            tamanho = input("Digite o tamanho da bandagem que deseja remover: ")
            estoque.remover_bandagem(cor, tamanho)
        
        elif escolha == "3":
            print("Selecione a bandagem que deseja alterar a quantidade:")
            estoque.consultar_estoque()
            index = int(input("Digite o número correspondente à bandagem: "))
            nova_quantidade = int(input("Digite a nova quantidade: "))
            estoque.alterar_quantidade(index, nova_quantidade)
        
        elif escolha == "4":
            estoque.consultar_estoque()
        
        elif escolha == "5":
            print("Encerrando o sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o menu interativo
menu()
