from utils import CurrencyConverter

real = float(input('Digite a quantidade de conversão: '))

print ('Em libra £{:0,.2f}'.format(CurrencyConverter.convert_to_libra(real)) )
print ('Em dolar ${:0,.2f}'.format(CurrencyConverter.convert_to_dollar(real)) )
print ('Em euro €{:0,.2f}'.format(CurrencyConverter.convert_to_euro(real)) )

