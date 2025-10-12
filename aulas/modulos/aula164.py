# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime('%d/%m/%Y')) #formato brasileiro
print(data.strftime('%d/%m/%Y %H:%M')) #formato brasileiro com horas e minutos
print(data.strftime('%d/%m/%Y %H:%M:%S')) #formato brasileiro com horas, minutos e segundos
print(data.strftime('%Y'), data.year) #formato americano
print(data.strftime('%d'), data.day) #dia
print(data.strftime('%m'), data.month) #mês
print(data.strftime('%H'), data.hour) #hora
print(data.strftime('%M'), data.minute) #minuto
print(data.strftime('%S'), data.second) #segundo