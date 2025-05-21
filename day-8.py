import random

def generate(len):
    all_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*@"
    password = ""
    for i in range(len):
        password += random.choice(all_chars)
    return password

len = int(input("Enter the length of the password: "))
password = generate(len)
print(f"Your password is: {password}")