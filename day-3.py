import random
import time

gap = time.sleep

no = int(input("Enter number of players: "))
players = []
<<<<<<< HEAD
gap(1)
for i in range(0 , no-1 , 1):
    players[i] = input(f"Enter player no.{i + 1} name :")
=======
>>>>>>> fb32e20209544ca5420811087aee828a88429997

gap(1)

for i in range(no):
    name = input(f"Enter player no.{i + 1} name: ")
    players.append(name)

dares = [
    "Do 20 squats", "Do 10 situps", "Do 5 pushups", "Slap yourself",
    "Sing a song", "Jump 20 times", "Make a silly face", "Talk in funny accent",
    "Try to balance a book on your head", "Tell a joke", "Tell a story"
]


playing = True
while playing == True :
    gap(1)
    player_no = random.randint(0, no - 1)

    print(f"\n It's {players[player_no]}'s turn:")
    gap(2)
    random_dare = random.choice(dares)
    print(random_dare)
    status = input("Continue game (y/n) :")
    if (status == "y"):
        playing = True
    elif(status == "n"):
        playing = False
     
    else:
        print("Invalid input write 'y' for yes and 'n' for no")        
        