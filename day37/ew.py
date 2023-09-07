import random
# s = "   +0 123       "
# print(s.strip())
# print(len(s.strip()))
# nums =["0","1","2","3","4","5","6","7","8","9"]
# count =0
# out_num=""
# if " " in s:
#     s=s.replace(" ","")
# if len(s)>0:
#     if "-" == s[0]:
#         sign,s=-1,s.replace("-","")
#     elif "+" == s[0]:  
#         sign,s=1, s.replace("+","")
#     else:
#         sign =1
# while count < len(s) and s[count].isdigit():
#         out_num =out_num+s[count]
#         count+=1
        
        
# print(out_num)
# if len(out_num)==0:
#     out_num =0
# # print(out_num)
# else:
#     new_str = sign*(int(out_num))
#     if -2**31<=new_str<=2**31 -1:
#         print(new_str)


# listted = [1,2,3,4]

# listed = random.shuffle()
# print(listed)
# mylist = [1, 2, 3]
# random.shuffle(mylist)

# print(mylist)

per =1
nums =[1,2,3]
final_list = []

for i in range(1,len(nums)+1):
    per*=i
    
# while per >1:
#     random.shuffle(nums)
#     if nums not in final_list:
#         final_list.append(nums)
#         per-=1

# print(final_list)


# while len(final_list)<per:
#     temporary_list = []
#     num = nums

#     while len(num)>0:
#         for i in range(len(nums)-2):
#             num,temporary_list = num[:i] +num[i+1:], temporary_list + [num[i]]
            
            
#     final_list.append(temporary_list)
    
        
# print(final_list)


# s = "anagram"
# t = "nagaram"

# seen = set(s)

# print(seen[1])

# coordinates =[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# x = coordinates[1][0] - coordinates[0][0]
# y = coordinates[1][1] - coordinates[0][1]

# slope = y/x
        
# for i in range(len(coordinates)-1):
#         new_x = coordinates[i+1][0] - coordinates[i][0]
#         new_y = coordinates[i+1][1] - coordinates[i][1]
#         new_slope = new_y/new_x
#         print(new_slope)
        
#         if new_slope!=slope:
#             print("False")
# print(slope)

listed = [1,2,3]
count_dict ={
            1:"I" ,
            5:"V" ,
            10:"X" ,
            50:"L",
            100:"C" ,
            500:"D" ,
            1000:"M",
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM",
            
        }

print(sorted(count_dict.keys())[::-1])

print()