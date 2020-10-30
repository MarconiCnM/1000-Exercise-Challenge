print('========= Read a speed in km/h and display it converted to m/s. ========= \n')

while True:
  try:
    velocity_kmh = int(input('Enter the amount to be converted:'))
    break
  except:
    print('\n*=*=*=* Oops! That was no valid number. Try again... *=*=*=*\n')

velocity_ms = velocity_kmh/3.6

print(f'\nThe value {velocity_kmh}km/h is equal to {velocity_ms}m/s.')