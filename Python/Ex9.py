print('========= Read a temperature in degrees Celsius and have it converted to degrees Kelvin. =========\n')

while True:
  try:
    degrees_celsius = float(input('Enter the amount to be converted: '))
    break
  except:
    print('\n*=*=*=* Oops! That was no valid number. Try again... *=*=*=*\n')

degrees_kelvin = degrees_celsius + 273.15

print(f'\nThe value {degrees_celsius}C is equal to {degrees_kelvin}K')