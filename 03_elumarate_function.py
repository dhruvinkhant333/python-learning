marks = [20, 25, 56, 75 ,47]

for index , mark in enumerate(marks):
    print(mark)
    if ( index == 3):
        print("good job leo")

#or 

# index = 0 
# for mark in marks :
#     print(mark)
#     if (index == 3):
#         print ("good job leo")
#         index +=1

#2nd example 

fruits = ['apple' , 'banana' , 'mango']
for number , fruit in enumerate(fruits):
    print ( number , fruit)


# By default enumerate start value with 0 but we can start with our specified starting index 


fruits = ['apple' , 'banana' , 'mango']
for number , fruit in enumerate( fruits , start = 1 ):
    print ( number , fruit )