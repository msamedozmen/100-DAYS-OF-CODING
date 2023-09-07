#Write your code below this line 👇
checkin_list=[]
def prime_checker(number):
    for i in range(1,number+1):
        if number % i ==0:
            checkin_list.append(i)
    if checkin_list == [1,number]:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

    print(checkin_list)



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
