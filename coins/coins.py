# name of student: Lars
# number of student: 99069312
# purpose of program: School
# function of program: Money
# structure of program: Python

toPay = int(float(input('Amount to pay: '))* 100) #Shows what you have to pay
payed = int(float(input('Payed amount: ')) * 100) #Shows what you have paid
change = payed - toPay #math
overview = "Overview: "

if change > 0: #If the change is more than 0 something happens
  coinValue = 500 # Gives the valuable a number
  
  while change > 0 and coinValue > 0: # When both are more than 0 
    nrCoins = change // coinValue #Math equasion 

    if nrCoins > 0: #When the answer of the equasion is more than 0 
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # Prints a text of your answers
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # Asks how many u returned
      change -= nrCoinsReturned * coinValue # math
      overview = str(overview) + str(nrCoins) + ' coins of ' + str(coinValue) + ' cents. '
# comment on code below: These are the coin values
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #IF change is more than 0
  print('Change not returned: ', str(change) + ' cents')
else:
  print(overview)
  print('done')