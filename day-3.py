#Random dare game
import random
import time
gap = time.sleep

no = int(input("Enter number of players:"))

players = []
gap(1)
for i in range(0 , no-1 , 1):
    players[i]=input(f"Enter player no.{i + 1} name :")

dares = ["Do 20 squats",
          "Do 10 situps",
            "Do 5 pushups",
            "Slap yourself",
            "Sing a song",
            "Jump 20 times",
            "Make a silly face",
            "Talk in funny accent",
            "Try to balance a book on your head ",
            "Tell a joke",
            "Tell a story"]
gap(1)

player_no= random.randint(0 , no-1)

print(f"{players[player_no]} should do this dare :")
gap(2)
random_dare = random.choice(dares)
print(random_dare)