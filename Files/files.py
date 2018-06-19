# Building a file path using OS module

import os
paths = os.path.join("/home", "terpgene", "Documents", "exercises", "Files", "st.txt" )
# st = open("st.txt", "w")
# st.write("Hi from Python")
# st.close()

with open(paths, "w") as file:
    file.write("Hi from Python!")


my_list = list()
with open(paths, "r") as file:
    my_list.append(file.read())

print(my_list)

