#this is typewritter effect
import time 
gap = time.sleep
text = input("Enter text : ")


for i in range(0 , len(text) , 1):
    gap(0.05)
    print(text[i] , end="", flush=True)