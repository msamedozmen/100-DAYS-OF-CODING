import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list=["Rock","Paper","Scissiors"]
images = [rock,paper,scissors]
user_chose = input("What do u chose? Type 0 for Rock, 1 for Paper and 2 for Scissiors ")
computer_chose = random.randint(0,2)

print("Your Chose/n", images[int(user_chose)])

if 2<int(user_chose) or 0>int(user_chose):
    print("You lose")
    
computer_chose = random.randint(0,2)
print("Computer Chose/n", images[int(computer_chose)])
computer_chose = list[computer_chose]
user_chose=list[int(user_chose)]

if user_chose == computer_chose:
    print("Draw!!!")
elif user_chose =="Rock" and computer_chose == "Scissiors":
    print("You win")
elif user_chose =="Rock" and computer_chose == "Paper":
    print("You lose")
elif user_chose =="Paper" and computer_chose == "Rock":
    print("You win")
elif user_chose =="Paper" and computer_chose == "Scissiors":
    print("You lose")
elif user_chose =="Scissiors" and computer_chose == "Rock":
    print("You lose")
else:
    print("You win")

