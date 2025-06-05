# this checks ordered pairs are equal or not 
# opt maths chapter 1 😁
import time

print("Check if two orderd pairs are equal or not");
time.sleep(2)
print("Enter the first ordered pair")
time.sleep(1)
a = int (input("Enter the first number:"))
b = int (input("Enter the second number:"))
time.sleep(0.5)
print("Enter the second ordered pair")
time.sleep(1)
c = int(input ("Enter the first number:"))

d = int(input ("Enter the second number:"))
time.sleep(1)
if a ==c and b==d :
    print("Those ordered pairs are equal")
else:
    print("Those ordered pairs are not equal")
