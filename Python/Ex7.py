print('========= Read a temperature in degrees Fahrenheit and display it converted to degrees Celsius. =========\n')

while True:
  try:
    degrees_fahrenheit = float(input('Enter the amount to be converted: '))
    break
  except:
    print('\n*=*=*=* Oops! That was no valid number. Try again... *=*=*=*\n')

degrees_celsius = 5 * (degrees_fahrenheit - 32) / 9

print(f'\nThe value {degrees_fahrenheit}F is equal to {degrees_celsius}C')