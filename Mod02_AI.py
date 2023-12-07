class BookStoreInvetory:
    def __init__(self):
        self.inventory = {}
    
    def addBook(self, title, quantity):
        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity
    def checkQuantity(self, title):
        if title in self.inventory:
            return self.inventory.get(title, 0)
        else:
            return 0
    def removeBook(self, title, quantity):
        if title in self.inventory and self.inventory[title] >= quantity:
            self.inventory[title] -= quantity
            if self.inventory[title] == 0:
                del self.inventory[title]
            return True
        return False
        
    def recommendBooks(self, description):
       # Esta é uma recomendação simulada baseada em palavras-chave na descrição 
        keywords = description.lower().split()
        recomendations = {
           'análise avançada': 'Os elementos da aprendizagem estatística',
           'aventura': 'O Hobbit de J.R.R. Tolkien',
           'mistério': 'As Aventuras de Sherlock Holmes de Arthur Conan Doyle',
           'romance': 'Orgulho e Preconceito de Jane Austen',
           'ficção científica': 'Duna de Frank Herbert',
           'fantasia': 'Harry Potter e a Pedra Filosofal de J.K. Rowling',
           'história': 'Sapiens: Uma Breve História da Humanidade por Yuval Noah Harari'
       }
        for keyword in keywords:
            if keyword in recomendations:
                return recomendations[keyword]
        return "Sem recomendações para você no momento."

if __name__ == "__main__":
    bookstore = BookStoreInvetory()
    bookstore.addBook("Sapiens: Uma Breve História da Humanidade", 5)
    bookstore.addBook("Duna", 3)
    bookstore.addBook("O Hobbit", 1)
    bookstore.addBook("O Senhor dos Anéis", 2)
    bookstore.addBook("Harry Potter e a Pedra Filosofal", 4)
    bookstore.addBook("As Aventuras de Sherlock Holmes", 3)
    
    recomendation = bookstore.recommendBooks("Este livro é uma aventura sobre um hobbit que encontra um anel mágico.")
    print("Recomendação: " + recomendation)
    hobbitQuantity = bookstore.checkQuantity("O Hobbit")
    print("Quantidade de O Hobbit: " + str(hobbitQuantity))
    bookstore.removeBook("O Hobbit", 1)
    print(hobbitQuantity, recomendation, bookstore.checkQuantity("O Hobbit"))