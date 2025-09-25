from log import LogPrintMixin, LogFileMixin

class eletronico:
    pass
    def __init__(self, nome):
        pass
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True
            print(f'{self._nome} está ligado.')
        else:
            print(f'{self._nome} já está ligado.')

    def desligar(self):
        if self._ligado:
            self._ligado = False
            print(f'{self._nome} está desligado.')
        else:
            print(f'{self._nome} já está desligado.')


class Smartphone(eletronico, LogFileMixin):
    pass
    def ligar(self):
        super().ligar()
        if self._ligado:
            msg = f'{self._nome} foi ligado com sucesso.'
            self.log_Success(msg)


    def desligar(self):
        super().desligar()
        if not self._ligado:
            msg = f'{self._nome} foi desligado com sucesso.'
            self.log_Error(msg)
