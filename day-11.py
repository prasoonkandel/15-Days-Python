import random
import pyttsx3

number = random.randint(1, 10)
engine = pyttsx3.init()
print("Guess a number between 1 and 10: ")
engine.say("Guess a number between 1 and 10 ")

engine.runAndWait()
guess = int(input())




if guess == number:
    print("🎉 Correct! You guessed it!")
    
    engine.say(" Correct! You guessed it!")
    engine.runAndWait()

else:
    print(f"❌ Wrong! The number was {number}.")
 
    engine.say(f"Wrong! The number was {number}.")
    engine.runAndWait()