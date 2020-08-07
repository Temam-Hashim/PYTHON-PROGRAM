#game 1
from random import randint
playerWin = 0
computerWin = 0
while(True):
  rand = randint(0,2)
  l = ['Rock','Paper','Scissor'] 
  computer = l[rand]
  print("enter X to exit")
  player = input("choose Rock,Paper or Scissor:")
  if(player==computer):
      print("Game is Tie No Winner")
  elif(player=='Rock'):
      if(computer=='paper'):
          print('Computer Win',computer,'wraps',player)
          computerWin+=1
      else:
          print('Player Win',player,'smashes',computer)
          playerWin+=1
  elif(player=='Paper'):
      if(computer=='Scissor'):
          print("Computer Win",computer,'cuts',player)
          computerWin+=1
      else:
          print('Computer Win',player,'smashes',computer)
          playerWin+=1
          
  elif(player=="Scissor"):
      if(computer=="Rock"):
          print("Computer Win",computer,'cut',player)
          computerWin+=1
      else:
          print('Player Win',player,'smashes',computer)
          playerWin+=1
  elif(player=="x"):
      exit()
  else:
      print("invalid Move")
  print("Number of player Win:",playerWin)
  print("Number of computer Win:",computerWin)
          
      
