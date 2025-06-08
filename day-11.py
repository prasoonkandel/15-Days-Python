
# bmi calculator by using functions  very nice
import time
gap = time.sleep

def bmi(weight , height):
    bmi = weight/(height*height)
    return bmi

def bmi_range(bmi):
    if(bmi<18.5):
        message ="You are underweight"   
    elif(bmi>18.5 and bmi<24.9):
        message = "Your weight is normal"
    elif(bmi>25 and bmi<29.9):
        message = "You are overweight"
    elif(bmi>=30):
        message="You are obese"
    else:
        message="Invalid inputs"    
    return message     

print("BMI calculator 💪🏼")   
gap(0.5)
weight = float(input("Enter your weight (kg):"))
height = float(input("Enter your height (m):"))

print("Calculating...", end='', flush=True)
bmi_val = bmi(weight, height)
rounded_bmi= round(bmi_val ,2)
gap(2)
print(f"\rYour BMI is {rounded_bmi}         \r")
bmi_message = bmi_range(bmi_val)
gap(1)
print(bmi_message)


