

def main(dice_rolls, dice_size):
  import random

#  dice_rolls = int(input('How many dice would you like to roll? '))
#  dice_size = int(input('How many sides are the dice? '))
  dice_sum = 0

  for i in range(0,dice_rolls):
      roll = random.randint(1,dice_size)
      if roll == 1:
          print(f'You rolled a {roll}! Critical Fail')
      elif roll == dice_size:
          print(f'You rolled a {roll}! Critical Success!')
      else:
          print(f'You rolled a {roll}')

      dice_sum += roll

  print(f'You have rolled a total of {dice_sum}')
  return dice_sum

if __name__== "__main__":
  players = int(input('How many players? '))
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))

  resultados = {}

  for i in range(0,players):
      #resultados.append(main(dice_rolls,dice_size))
      jugador = "player"+str(i+1)
      resultados[jugador] = main(dice_rolls,dice_size)

print(resultados.items())
