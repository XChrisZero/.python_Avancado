# Mantendo estados dentro da classe
class Camera: # Classe
    def __init__(self, nome, filmando=False): # Construtor
        self.nome = nome
        self.filmando = filmando

    def filmar(self): # Método
        if self.filmando: # Verifica o estado
            print(f'{self.nome} JÁ está filmando...')
            return

        print(f'{self.nome} está filmando...')
        self.filmando = True # Atualiza o estado

    def parar_filmar(self): # Método
        if not self.filmando: # Verifica o estado
            print(f'{self.nome} NÃO está filmando...')
            return

        print(f'{self.nome} está parando de filmar...')
        self.filmando = False # Atualiza o estado

    def fotografar(self): # Método
        if self.filmando: # Verifica o estado
            print(f'{self.nome} não pode fotografar filmando') 
            return

        print(f'{self.nome} está fotografando...')


c1 = Camera('Canon') # Instância
c2 = Camera('Sony') # Instância

c1.filmar() # Método
c1.filmar() # Método
c1.fotografar() # Método
c1.parar_filmar()   # Método
c1.fotografar() # Método

print()

c2.parar_filmar()  # Método
c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()