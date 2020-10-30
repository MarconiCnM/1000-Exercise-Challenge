print('========= Read a temperature in Kelvin and have it converted to degrees Celsius. =========\n')

while True:
  try:
    degrees_kelvin = float(input('Enter the amount to be converted: '))
    break
  except:
    print('\n*=*=*=* Oops! That was no valid number. Try again... *=*=*=*\n')

degrees_celsius = degrees_kelvin - 273.15

print(f'\nThe value {degrees_kelvin}K is equal to {degrees_celsius}C')