import wizcoin

purse = wizcoin.WizCoin(2,5,99) # The ints are passed to __init__().
print("purse = ",purse)
print('G:', purse.galleons, 'S:', purse.sickles, 'K:', purse.knuts)
print('Total value:', purse.total())
print('Total value:', purse.total2) # using @property
print('Weight:', purse.weightInGrams(), 'grams')
print()

coinJar = wizcoin.WizCoin(13,0,0) # The ints are passed to __init__().
print("coinjar = ",coinJar)
print('G:', coinJar.galleons, 'S:', coinJar.sickles, 'K:', coinJar.knuts)
print('Total value:', coinJar.total())
print('Total value:', coinJar.total2) # using @property
print('Weight:', coinJar.weightInGrams(), 'grams')
