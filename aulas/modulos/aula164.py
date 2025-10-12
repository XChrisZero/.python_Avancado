# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(type(data.strftime('%d/%m/%Y'))) #de tipo string
print(data.strftime('%d/%m/%Y')) #formato brasileiro
print(data.strftime('%d/%m/%Y %H:%M')) #formato brasileiro com horas e minutos
print(data.strftime('%d/%m/%Y %H:%M:%S')) #formato brasileiro com horas, minutos e segundos
print(data.strftime('%Y'), data.year) #data.year é do tipo inteiro
print(data.strftime('%d'), data.day) #data.day é do tipo inteiro
print(data.strftime('%m'), data.month) #data.month é do tipo inteiro
print(data.strftime('%H'), data.hour) #data.hour é do tipo inteiro
print(data.strftime('%M'), data.minute) #data.minute é do tipo inteiro
print(data.strftime('%S'), data.second) #data.second é do tipo inteiro