import datetime
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o metodo _log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
   
    def log_success(self, msg):
        return self._log(f'Sucess: {msg}')
    
class logPrintMixin(Log):
    def _log(self, msg):
        dia_hora = datetime.datetime.now()
        print(f'{msg} / {dia_hora}')

class logFileMixin(Log):
    def _log(self, msg):
        dia_hora = datetime.datetime.now()
        msg_formatada = f'{msg} / {dia_hora}'
        with open(LOG_FILE, 'a') as file:
            file.write(msg_formatada)
            file.write('\n')
        
if __name__ == '__main__':
    l = logPrintMixin()
    l.log_error('log error implementado')
    l.log_success('log success implementado')
    lf = logFileMixin()
    lf.log_error('log error implementado')
    lf.log_success('log success implementado')
    
    