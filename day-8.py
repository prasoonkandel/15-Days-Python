#password generator
import random

def generate(len):
    all_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&*@"
    password = ""
    for i in range(len):
        password += random.choice(all_chars)
    return password

len = int(input("Enter the length of the password: "))
less_length = False
if len < 6:
    less_length=True
    while less_length==True:
        print("Please at least 6 characters")
        len = int(input("Enter the length of the password: "))
        if len >= 6:
            break
else:
    less_length=False
password = generate(len)
print(f"Your password is: {password}")