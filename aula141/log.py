#Abstração
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


#log
class Log:
    def _log(self, msg):
        raise NotImplementedError('Você deve implementar o método log.')
    
    def log_Error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_Success(self, msg):
        return self._log(f'Success: {msg}')
    


#filelog
class LogFileMixin(Log):
    def _log(self, msg): 
        msg_format = f'({self.__class__.__name__}): Logando... {msg}.\n'
        print(f'Salvando no log... {LOG_FILE}')
        with open(LOG_FILE, 'a') as arquivo: # with open é usado para garantir que o arquivo seja fechado corretamente após o uso, as arquivo é fechado automaticamente quando o bloco with é finalizado.
            arquivo.write(msg_format) # write adiciona o texto ao final do arquivo
            arquivo.write('\r\n')


#printlog
class LogPrintMixin(Log):
    def _log(self, msg): 
        print(f'({self.__class__.__name__}): Logando... {msg}.')
        print()



if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_Error('Mio familia!') 
    lp.log_Success('Deu bom familia!')

    lf = LogFileMixin()
    lf.log_Error('Mio familia!')
    lf.log_Success('Deu bom familia!')
