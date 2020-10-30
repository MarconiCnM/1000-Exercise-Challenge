print('========= Read a real number and print the fifth part of that number. ========= \n')

while True:
  try:
    real_number = float(input('Enter a real number: '))
    break
  except:
    print('\n*=*=*=* Oops! That was no valid number. Try again... *=*=*=*\n')

result = real_number / 5 

print(f'\nThe fifth part of this number is equal to {result}')