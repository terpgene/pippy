# Building a file path using OS module

import os
import csv 

csvpath = os.path.join("/home", "terpgene", "Documents", "exercises", "Files", "self_taught.csv")
paths = os.path.join("/home", "terpgene", "Documents", "exercises", "Files", "st.txt" )
# st = open("st.txt", "w")
# st.write("Hi from Python")
# st.close()



with open(paths, "w") as file:
    file.write("Hi from Python!")

# with open(csvpath, "w") as f:
#     file.write("one,two,three four,five,six")

my_list = list()
with open(paths, "r") as file:
    my_list.append(file.read())

print(my_list)

with open(csvpath, "w", newline='') as f:
    w = csv.writer(f, 
                    delimiter=",")
    w.writerow(["One",
                "two",
                "three"])
    w.writerow(["four",
                "five",
                "six"])


with open(csvpath, "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

