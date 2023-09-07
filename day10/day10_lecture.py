"""
def format_name(f_name,l_name):
    print(f_name.title())
    print(l_name.title())
    
    
format_name("angela","yu")
"""


def format_name(f_name,l_name):
    formated_namel = l_name.title()
    formated_namef =f_name.title()
    return f"Your name is : {formated_namef} {formated_namel}"
    
    
print(format_name("muhammed samed","OZMEN"))
