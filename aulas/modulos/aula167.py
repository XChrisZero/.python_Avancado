# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
import calendar
import locale

#deixando em branco pega a localidade do sistema
locale.setlocale(locale.LC_ALL, 'tr_TR') # Define a localidade para todas as categorias
print(locale.getlocale()) # Pega a localidade atual
#print(locale.locale_alias) # Mostra todas as localidades possíveis
print()

print(calendar.calendar(2022))