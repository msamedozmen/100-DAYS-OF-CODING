# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]
# lenght_l1 = len(l1)
# lenght_l2 = len(l2)
# listed =[]
# class Calculation:
#     def __init__(self,list1,list2):
#         self.listed = []
#         self.liste1 = list1
#         self.liste2 =list2
#         for i in range(len(list1)):
#             sum = self.liste1[i] +self.liste2[i]
#             if sum< 10:
#                 self.listed.append(sum)
#             else:
#                 try:
#                     self.liste1[i+1] = self.liste1[i+1]+ int(sum/10)
#                     print(self.liste1[i+1])
#                     self.listed.append(sum%10)
#                 except IndexError:
#                     self.listed.append(sum-10)
#                     self.listed.append(int(sum/10)) 

# if lenght_l1> lenght_l2:
#     for i in range(lenght_l2,lenght_l1):
#         l2.append(0)
#     calc = Calculation(l1,l2)

#     print(calc.listed)

# elif lenght_l1 == lenght_l2:
#     calc = Calculation(l1,l2)

#     print(calc.listed)

# else:
#     for i in range(lenght_l1,lenght_l2):
#         l1.append(0)
#     calc = Calculation(l2,l1)

#     print(calc.listed)
        
# s="([{}])"


# a="()"
# b="[]"
# c="{}"

# count = len(s)

# # if c in s:
# #     print("yep")
# #     s= s.replace(c,"")
# while count>1:
#     if a in s:
#         s=s.replace(a,'')
#     if b in s:
#         s=s.replace(b,'')
#     if c in s:
#         s=s.replace(c,'')
#     count-=1
    
# if len(s)!= 0:
#     print(False)
# else:
#     p
#     if char not in
    

# final_substring=[]
# all_substring =[]
# longest_substring = []
# count = len(s)
# while len(s)>0:
#     # new_s = s
#     for char in new_s:
#         if char not in longest_substring: 
#             longest_substring.append(char)
#             new_s=new_s[1:]
                
#         else:
#             all_substring.append(longest_substring)
#             longest_substring=[]
#             longest_substring.append(char)
#             new_s=new_s[1:]
#     all_substring.append(longest_substring)
#     longest_substring=[]
#     s=s[1:]
            

# a=0
# for list in all_substring:
#     if a< len(list):
#         a= len(list)   
#         final_substring = list   

# substring = "".join(final_substring)

# print(substring)

# nums =[11,122,33,44,44]
a="abcdsf"
b="cab"
print(a.index("ab"))
print(b.index("ab"))
# # for char in nums:
# #     locations=[]
# #     for location, value in enumerate(nums):
# #         if  value == char:
# #             locations.append(location)
# #     print(locations)


# print(sorted(nums))


# nums = [4,1,-1,2,-1,2,3]

# nums = sorted(nums)
# print(nums)
# count=0
# same_num =nums[0]
# sum={}
# for num in nums:
#     if num == same_num:
#         count+=1
#         if num is nums[-1]:
#             sum[same_num]= count        
#     else:
#         sum[same_num]= count
#         same_num = num
#         count =1
#         if num is nums[-1]:
#             sum[same_num]= count

# sum=dict(sorted(sum.items(),key=lambda x:x[1],reverse=True))
# print(sum)
# # sum =sorted(sum,reverse=True)

# # x = [key for (key,value) in sum]
# x=list(sum.keys())
# print("x",x)


# # print(sorted(sum.items()))

# #     # if same
            
# nums = [-1,0,1,2,-1,-4]        
# sum_list = []
# for i in range(len(nums)-2):
#     for j in range(i+1,len(nums)-1):
#         for k in range(j+1,len(nums)):
#             if nums[i] + nums[j] + nums[k] ==0:
#                 if len(sum_list)>0:
#                     for item in sum_list:
#                         if sorted([nums[i],nums[j],nums[k]]) not in sorted(item):
#                             print(sorted([nums[i],nums[j],nums[k]]))
#                             print(sorted(item))
#                             sum_list.append([nums[i],nums[j],nums[k]])
#                 if len(sum_list) ==0:
#                      sum_list.append([nums[i],nums[j],nums[k]])
                     
# print(sum_list)


# print(sorted([nums[1],nums[2],nums[5]]))
# print(sorted(sum_list[1]))

# # if sorted(sum_list[0])== sorted(sum_list[2]):
# #     sum_list.remove(sum_list[2])
# # print(sum_list) 

# print(sorted(sum_list))

# if __name__ == '__main__':
#     s ="Car"
#     s = ''.join(filter(str.isalnum, s)).lower()

# print(s[::-1])
# print(s)
