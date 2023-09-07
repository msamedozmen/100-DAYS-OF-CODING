# from selenium import webdriver
# from selenium.webdriver.common.by import By

# name_list = []
# time_list = []


# option = webdriver.ChromeOptions()
# option.add_experimental_option("detach",True)

# driver = webdriver.Chrome(options=option)


# driver.get("https://www.python.org/")


# times = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
# names = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")

# for time in times:
#     time_list.append(time.text)
# # print(time)


# for name in names:
#     name_list.append(name.text)
    
# dict = {i:{"name":name_list[i],"time":time_list[i]} for i in range(len(time_list))}

# print(dict)
total_dict = {'Cursor ': 15, 'Grandma ': 165, 'Factory ': 500}
print(list(total_dict.keys())[list(total_dict.values()).index(max(total_dict.values()))])