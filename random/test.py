
# original program 
def read_grade(module_code):
    grade = int(input(f'{module_code} Grade: ' ))
    if not 0 <= grade <= 100:
        raise ValueError
    return grade 

cmm201 =read_grade ('CMM201')
cmm202 = read_grade('CMM202')
avg = (cmm201 + cmm202) / 2 
print( f'Your average grade is {avg}')

# here are the defects in this program 
                    # 1
# if a digit greater than 100  or less than 0 is added it crashes 

                    # 2
# the variables are badly named 

                    #3
# if a user writes something different from a number, it crashes 
                    #4
# it badly structured, only a programmer can understand the programme 
 