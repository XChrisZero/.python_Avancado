# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
from functools import partial # para criar funções parciais


class Foo:
    def __init__(self):
        self.public = 'isso é público' # pode ser usado em qualquer lugar
        self._protected = 'isso é protegido' # não DEVE ser usado fora da classe
        self.__private = 'isso é privado' # só DEVE ser usado na classe em que foi declarado

    def metodo_publico(self): # pode ser usado em qualquer lugar
        print(self.public)
        return 'metodo_publico'

    def _metodo_protected(self): # não DEVE ser usado fora da classe
        print(self._protected)
        return '_metodo_protegido'

    def __metodo_private(self): # só DEVE ser usado na classe em que foi declarado
        print(self.__private)
        return '__metodo_privado'


f = Foo()
print(f.public)
print(f.metodo_publico()) # o metodo é público
print('---')
### FUNCIONA! mas NÃO DEVE ser usado fora da classe ###
print(f._protected, "e NÃO DEVE ser usado fora da classe") 
print(f._metodo_protected()) # NÃO DEVE ser usado fora da classe
print('---')
print(f._Foo__private, "e SÓ DEVE ser usado na classe em que foi declarado") 
print(f._Foo__metodo_private()) # SÓ DEVE ser usado na classe em que foi declarado
print('---')