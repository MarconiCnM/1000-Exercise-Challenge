print('========= Read a real number and print the result of the square of that number. =========\n')

while True:
  try:
    real_number = float(input('Enter a real number: '))
    break
  except:
    print('\n*=*=*=* Oops! That was no valid number. Try again... *=*=*=*\n')

result = real_number ** 2

print(f'\nThe square of this number is equal to {result}.') 