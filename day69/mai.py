import random 


took = ["a","b","c","d","e"]
give = ["a","b","c","d","e"]
# giver = random.choices(players,k=2)
# while len(players)>0:
#     giver = random.choices(not_give,2)
#     for person in giver:
#         not_give.remove(person)
#     taker = random.choices(not_give,k=2)
#     for pers in taker:
#         not_took.remove(pers)
    
#     result.append

random.shuffle(give)
print(give)
print(took)
is_not = True
# while is_not:
print(give!=took)
if give != took:
    print("y")
    # result = [[give[i],took[i]] for i in range(len(took))]
    # is_not = False

# else:
#     random.shuffle(took)
        

# # print(result)