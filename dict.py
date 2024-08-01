import json

data = json.load(open("data.json"))

while True:
    user_input = input("Please enter an English word to know its full meaning. Enter 'exit' to quit: ")
    if user_input == "exit":
        break
    else:
        print(data[user_input], "\n")




