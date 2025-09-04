#roll a 6 sided die->if its less than or equals to 4 you lose a hundred dollars but if its more than 4 you win $102.
import matplotlib.pyplot as plt
import random
plt.clf()
diceRolls=[]
for y in range(0,500):
  dice=[0]
  for x in range(0,50):
    choose=random.randint(1,6)
    if choose <=4:
      dice.append(dice[-1] -100)
    else:
      dice.append(dice[-1] +102)
  diceRolls.append(dice)
transposed_lists = list(map(list, zip(*diceRolls)))
averages = [sum(items) / len(items) for items in transposed_lists]
plt.plot(averages)
plt.show()
