# numbers = [1,2,3]

# new_list =[i**3 for i in numbers]

# print(new_list)



# doubled_list = [i*2 for i in range(1,5)]
# print(doubled_list)

# names = ["Samet","Yunus Emree", "Ahmet Mustafa", " Ali Murat","Aysel","Haydar","Necla"]


# name_list =[name for name in names if len(name)>5]

# # print(name_list)

# import random

# score={name:random.randint(1,100) for name in names}

# print(score)

# passed_students={key:value for (key,value) in score.items() if value>50}

# print(passed_students)


import pandas


student_dict ={
    "name": ["Samed","AHMET","Emre"]
    "score": [80,90,100]

}


student_frame = pandas.DataFrame(student_dict)