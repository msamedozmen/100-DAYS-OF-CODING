#Scope
enemies =1
def increase_enemies():
    enemies =2
    print(enemies)
    
increase_enemies()
print(enemies)

#local Scope

def drink_potion():
    potion_strenght = 2
    print(potion_strenght)
drink_potion()
print(potion_strengt) # will give error due to local scope 



#Global Scope