import random
from high_lover_logo import logo,vs
from game_data import data
# 'description'
# 'country'
# 'name'
used_person = []
pick_person= random.randint(0,len(data))
first_person = data[pick_person]
print(first_person['follower_count'])
used_person.append(first_person)
member_count=1
score =0
while member_count>0:
    pick_2nd_person= random.randint(0,len(data)-1)
    second_person = data[pick_2nd_person]
    if second_person not in used_person:
        used_person.append(second_person)
        
        member_count = 0
    else:
        member_count =1
        
print(f"Compare A: {first_person['name']}, a {first_person['description']}, and {first_person['country']} ")
print(vs)
print(f"Compare B: {second_person['name']}, a {second_person['description']}, and {second_person['country']} ")
player_guess = input("Who has more followers type 'A' or 'B'").lower()
if player_guess == "a":
    if first_person['follower_count']>second_person['follower_count']:
        score = score +1
        print(f"You're right. Current Score: {score}")

    else:
        print(f"You are wrong.Final score : {score}")
        quit
if player_guess == "b": 
    if second_person['follower_count']>first_person['follower_count']:
        score = score +1
        print(f"You're right. Current Score: {score}")
    else:
        print(f"You are wrong.Final score : {score}")
        quit
first_person = second_person
    
while True:
    member_count=1
    while member_count>0:
        pick_2nd_person= random.randint(0,len(data)-1)
        second_person = data[pick_2nd_person]
        if second_person not in used_person:
            used_person.append(second_person)
            member_count = 0
        else:
            member_count =1
        
    print(f"Compare A: {first_person['name']}, a {first_person['description']}, and {first_person['country']} ")
    print(vs)
    print(f"Compare B: {second_person['name']}, a {second_person['description']}, and {second_person['country']} ")
    player_guess = input("Who has more followers type 'A' or 'B'")
    if player_guess == "a":
        if first_person['follower_count']>second_person['follower_count']:
            score = score +1
            print(f"You're right. Current Score: {score}")

        else:
            print(f"You are wrong.Final score : {score}")
            break
    if player_guess == "b": 
        if second_person['follower_count']>first_person['follower_count']:
            score = score +1
            print(f"You're right. Current Score: {score}")
        else:
            print(f"You are wrong.Final score : {score}")
            break
    first_person = second_person
        