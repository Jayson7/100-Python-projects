a = "my name is feranmi otudeko"
print(a)

x = "Hello, World!" #Square brackets can be used to access elements of the strings
print(x[2]) #i.e its printing the letter (l) in HELLO, WORLD!

#Looping through a string
for x in "AsusRog":
    print(x)
    
#Length of a String using len()
x = "AsusRog"
print(len(x))

c = "Hello , World!"
print(len(c))

#Checking a string using the keyword 'in'
c = "Hello , World!"
print("tour" in c)
print("Hello" in c)
      #Using the 'if' statement to check a string using 'in'
if "tour" in c:
    print("Yes,tour is present.")
else:
    print("No,tour is not present.")
    
if "Hello" in c:
    print("Yes,Hello is present.")
else:
    print("No,Hello is not present.")    

#Checking a string using the keyword 'not in'    
c = "Hello , World!"
print("tour" not in c)
print("Hello" not in c)
      #Using the 'if' statement to check a string using 'not in'
if "tour" not in c:
    print("No,tour is not present.")
else:
    print("Yes,tour is  present.")
    
if "Hello" not in c:
    print("No,Hello is not present.")
else:
    print("Yes,Hello is present.")    

#Slicing a string from the start
x = "Hello, Worlds!" #so all letters btw (1-7) including space is been counted
print(x[1:7]) #i.e ELLO, + the space after the comma(,). 
#By leaving out the start index, the range will start at the first character.

#Slicing a string to the end
x = "Hello, Worlds!" # All letters after L will be excuted or shown cause we are slicing the string from L to the end of the string S!
print(x[2:]) #By leaving out the end index, the range will go to the end.

#Negative Indexing 
x = "Hello, Worlds!"  #Use negative indexes to start the slice from the end of the string
print(x[-4:-1]) 

#Modifiying a String(Upper Case)
y = "jack reaper"
print(y.upper())

#Modifiying a String(Lower Case)
y = "Jack REAPER"
print(y.lower())

#Modifiying a String(Remove White space)
y = " jack  reaper "  #Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
print(y.strip())














