from log import logFileMixin, logPrintMixin

l = logPrintMixin()
l.log_error('log error implementado')
l.log_success('log success implementado')

lf = logFileMixin()
lf.log_error('log error implementado')
lf.log_success('log success implementado')