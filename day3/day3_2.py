# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight/ (height*height)

if BMI <18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif 18.5< BMI <25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif 25< BMI <30:
    print(f"Your BMI is {BMI}, you are a slightly overweight.")
elif 30< BMI <35
    print(f"Your BMI is {BMI}, you are obese")
else: 
    print(f"Your BMI is {BMI}, you are clinically obese.")