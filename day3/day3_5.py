# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
count_list1 =["t","r","u","e"]
count_list2 =["l","o","v","e"]

lowered_name1 = name1.lower()
lowered_name2 = name2.lower()
count1=0
count2=0
for letter in count_list1:
    count1 += lowered_name1.count(letter)
    count2+= lowered_name2.count(letter)
count3=0
count4=0
for x in count_list2:
    count3 += lowered_name1.count(x)
    count4+= lowered_name2.count(x)
    
    
True_count = (count1+count2)*10 + count3 + count4

if 10>True_count or 90<True_count:
    print(f"Your score is {True_count}, you go together like coke and mentos.")
elif 40<True_count<50: 
    print(f"Your score is {True_count}, you are alright together.")
else:
 print(f"Your score is {True_count}.")
    