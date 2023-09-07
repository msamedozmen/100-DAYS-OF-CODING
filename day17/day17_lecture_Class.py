class User:
    def __init__(self,user_id,username):
        print("New user have been creating")
        self.id = user_id
        self.username = username
        self.followers =0
        self.following = 0
        
    def follow(self,user):
        user.followers +=1
        self.following += 1        
        
user_1= User("01","Samet")
user_2 = User("02","Murat")

user_1.follow(user_2)

print(user_2.following)
print(user_2.followers)
print(user_1.following)
print(user_1.followers)