# EXERCICIO DE POO PRODUTOS - AUTOR: Augusto dos Santos Barbosa

class Produto():
    def __init__(self, codigo:int, descricao:str, valor:float):
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor
    def imprimir(self):
        print("\nCodigo: ",{self.codigo}, "Descricao: ",{self.descricao}, "Valor: ",{self.valor})

class Eletronico(Produto):
    def __init__(self,codigo: int, descricao:str, valor:float, voltagem:int):
        super().__init__(codigo, descricao, valor)
        self.voltagem = voltagem
    def imprimir(self):
        super().imprimir()
        print("Voltagem:  ",{self.voltagem})
        

class Vestuario(Produto):
    def __init__(self, tamanho:str, codigo:int, descricao:str, valor:float, nome:str, cor:str):
        super().__init__(codigo, descricao, valor)
        self.tamanho = tamanho
        self.nome = nome
        self.cor = cor
    def imprimir(self):
        super().imprimir()
        print("Tamanho: ",{self.tamanho}, "Nome: ",{self.nome}, "Cor: ",{self.cor})


class Calcado(Vestuario):
    def __init__(self, tamanho:str, codigo:int, descricao:str, valor:float, nome:str, cor:str, materialsola:str, materialpartesuperior:str, materialinterior:str):
        super().__init__(codigo, valor,descricao,nome, cor, tamanho)
        self.materialsola = materialsola
        self.materialpartesuperior = materialpartesuperior
        self.materialinterior = materialinterior
    def imprimir(self):
        super().imprimir()
        print(f"Material da Sola: {self.materialsola}\nMaterial da Parte Superior: {self.materialpartesuperior}\nMaterial do Interior: {self.materialinterior}\n")
        
class Roupa(Vestuario):
    def __init__(self, tamanho:str, codigo:int, descricao:str, valor:float, nome:str, cor:str, tecido:str):
        super().__init__(codigo,descricao,valor,nome,cor,tamanho)
        self.tecido = tecido
    def imprimir(self):
        super().imprimir()
        print("Tecido: ", {self.tecido})
            

geladeira = Eletronico(1, "Geladeira Eletrolux", 3000, 110)
geladeira.imprimir()

microondas = Eletronico(2, "Microondas Eletrolux", 800, 220)
microondas.imprimir()

camisa = Vestuario("M", 3, "Camisa", 179, "Polo Nike", "Azul")  
camisa.imprimir()

calca = Vestuario("42", 4, "Calca Sarja", 249, "Jeans", "Preta")
calca.imprimir()

jordan = Calcado("All black", "41", "Jordan 11", 5, 2300, "Calcado", "Borracha", "Couro", "Tecido") 
jordan.imprimir()
airmax = Calcado("Branco e azul", "40", "Air Max Plus", 6, 1299, "Calcado", "Borracha", "Couro", "Tecido")   
airmax.imprimir()

blusa = Roupa("Blusa", "M", 7, "Blusa Overcome", 399, "Cinza", "Algodao")
blusa.imprimir()
short = Roupa("Short", "42", 8, "Short Adidas Essentials", 70, "Preto", "Algodao")
short.imprimir()




        



