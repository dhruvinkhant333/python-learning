
# import os
# import pandas as pd

# # file1 = open("student.txt", "w")
# # file1.write("Rahul\n")
# # file1.write("Amit\n")
# # file1.write("Neha\n")
# # file1.close()
# # print("File created successfully.")

# # file = open("student.txt", "r")

# # data = file.read()
# # print(type(data))
# # print(data)
# # file.close()

# # data = {
# #  "RollNo": [101, 102, 103, 104],
# #  "Name": ["Amit", "Neha", "Rahul", "Priya"],
# #  "Marks": [85, 90, 78, 95]
# # }
# # df = pd.DataFrame(data)
# # df.to_csv("Mystudents.csv", index=False)
# # print("CSV file created successfully.")
# # print("File Path:", os.path.abspath("Mystudents.csv"))


# # with open("student.dat" , "wb") as file : 
# #     pickel.dump(file, data)

# # print("data written succesfully!")



# # with open("student.dat" , "rb") as file : 
# #     print(file)


# # import random
# # print(random.random())

# # print(random.randrange(1,20)) # 20 is not included
# # print(random.randrange(1,20,2)) # 20 is not included, Odd numbers only

# # print(random.randint(1,20))

# from scipy import stats
# data = [10, 20, 30, 40, 50]
# result = stats.tmean(data)
# print("Mean:", result)

n = 5
fact = 1
for i in range(1,n+1):
    fact = fact*i

print(fact)