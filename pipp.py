# home = "Thailand"
# if home == "Japan":
#     print("Hello, Japan")
# elif home == "Thailand":
#     print("Hello, Thainland!")
# elif home == "India":
#     print("Hello, India!")
# elif home == "China":
#     print("Hello, China")
# else:
#     print("Hello, World!")
#
# colors = ["blue", "green", "yellow"]
# print(colors)
#
# colors[2] = "red"
# print(colors)
#
# colors1 = ["orange", "pink", "black"]
#
# print(colors + colors1)
#
# green = "green"  not in colors
# print(green)





colors2 = ["purple",
           "orange",
           "green"]

guess =  input("Guess a color: ")
if guess in colors2:
    print("You guessed correctly!")
else:
    print("Wrong! Try again.")
