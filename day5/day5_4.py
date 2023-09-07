#Write your code below this row 👇

numbers =list()

for i in range(1,101):
    numbers.append(i)

for number in numbers:
    if number%3 == 0 and number%5!=0:
        print("Fizz")
    elif number%5 ==0 and number%3!=0:
        print("Buzz")
    elif number%15 ==0:
        print("FizzBuzz")
    else:
        print(number)