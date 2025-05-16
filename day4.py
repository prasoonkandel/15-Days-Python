import time
import random
gap = time.sleep
#head or tails
print("This is a simple head or tails game")
gap(1)
user_side = input("Heads or tails (h/t):")
comp_side = random.randint(0 ,1)
if (user_side=="h" ):
    user_side = int(0)
else:
      user_side = int(1)
gap(2)      

if (user_side == comp_side):
     print("You won")
else:
     print("You lost")     