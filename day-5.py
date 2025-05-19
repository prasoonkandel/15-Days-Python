#diceroller
import random
import time
gap = time.sleep
print("🎲 Dice Roller Simulator")
playing = True
while playing == True :
  
    input("Press enter to roll dice")
    gap(1)
    dice = random.randint(1 , 6)
    print(f"You rolled {dice}")
    status = input("Press enter to roll again:")
    if (status == ""):
        playing = True
    else:
        playing = False
     
   
        
