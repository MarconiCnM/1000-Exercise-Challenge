print('========= Ask the user to enter a three integer values and print the sum of them. =========\n')

while True:
  try:
    number1 = int(input('Enter the first number: '))
    number2 = int(input('Enter the second number: '))
    number3 = int(input('Enter the third number: '))
    break
  except:
    print('\n*=*=*=* Oops! That was no valid number. Try again... *=*=*=*\n')

resultado = (number1 + number2 + number3)

print(f'\nThe sum of {number1} plus {number2} plus {number3} is equal to {resultado}.')