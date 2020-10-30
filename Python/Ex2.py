print('========= Make a program that reads a real number and prints it. =========\n')

while True:
  try:
    number = float(input("Please enter a number: "))
    break
  except ValueError:
    print('\n*=*=*=* Oops! That was no valid number. Try again... *=*=*=*\n')

print(f'\nThe number entered was {number}.')