"""
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
sum=0
for i in range(0,len(two_digit_number)):

    sum = sum+ int(two_digit_number[i])
# 🚨 Don't change the code above 👆
print(sum)
####################################
#Write your code below this line 👇

"""

print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
tip = input("What percentage tip would u like to give? 10, 12, 15? ")
count= input("How many people will split the bill? ")

bill= ((float(total_bill))*(100+ float(tip)))/100124.56

pay = bill / float(count)

pay =round(pay,2)
print(f"Each person should pay: {pay}")