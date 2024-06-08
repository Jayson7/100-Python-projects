# #x = 25
# #b = 26
# #if x>=25:
# #    print(x)
# else:
#     print(0)

# get the user input
x = input('Enter a number from range 1 - 10: ')
# convert the input to an integer
x = int(x)
if x in range(1, 11):
    print('valid input')
else:
    print('invalid input')

