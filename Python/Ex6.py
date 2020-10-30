print('========= Read a temperature in degrees Celsius and display it converted to degrees Fahrenheit. =========\n')

while True:
  try:
    degrees_celsius = float(input('Enter the amount to be converted: '))
    break
  except:
    print('\n*=*=*=* Oops! That was no valid number. Try again... *=*=*=*\n')

degrees_fahrenheir = degrees_celsius * (9/5) + 32

print(f'\nThe value {degrees_celsius}Cº is equal to {degrees_fahrenheir}Fº')
