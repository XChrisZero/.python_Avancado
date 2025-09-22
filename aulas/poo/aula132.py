# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯
class Caneta:
    def __init__(self, cor):
        # private protected
        self.cor = cor
        self._cor_tampa = None # sem q usar um underline antes do nome do atributo deve ser usado apenas na classe

    @property # para usar um getter, tem que ter o decorador @property
    def cor(self): # getter
        print('ESTOU NO GETTER')
        return self._cor # atributo protegido (por convenção)

    @cor.setter # para usar um setter, tem que ter o decorador @<nome do atributo>.setter
    def cor(self, valor): # setter
        #if valor == 'alguma cor': 
        #    raise ValueError('Cor inválida')
        print('ESTOU NO SETTER')
        self._cor = valor # atributo protegido

    @property 
    def cor_tampa(self): # getter
        return self._cor_tampa # atributo protegido

    @cor_tampa.setter # setter
    def cor_tampa(self, valor): # setter
        self._cor_tampa = valor # atributo protegido

#############################################
caneta = Caneta('Azul') # __init__ chama o setter
caneta.cor = 'Rosa' # chama o setter
caneta.cor_tampa = 'Azul' # chama o setter
print(caneta.cor) # chama o getter
print(caneta.cor_tampa) # chama o getter