import json
import time
from difflib import get_close_matches

# Load the data from the JSON file in 'data' veriable
data = json.load(open("data.json"))

# Define a function to translate the word
def translate(w):
    w = w.lower()  # Convert the word to lowercase to ensure case-insensitivity
    if w in data:  # Check if the word exists in the data
        print(f"Full meaning of '{w.capitalize()}' is:") #Capitalize the word so it looks good!
        for result in data[w]:  # Print all meanings of the word
            print("- ", result)
        return ""  # Return an empty string to avoid printing 'None'
    else:
        best_match = get_close_matches(w, data)  # Find close matches for the word
        if best_match:  # Check if there are any close matches
            match_input = input(f"Did you mean {best_match}? Please choose & input correct word: ")
            if match_input in best_match:  # Check if the user input is one of the close matches
                print(f"Full meaning of '{match_input}' is:")
                for result in data[match_input]:  # Print all meanings of the matched word
                    print("- ", result)
                return ""  # Return an empty string to avoid printing 'None'
            else:
                return "Please run again"
        else:
            return "Sorry! the word doesn't exist. Please check the spelling."

# Main loop to repeatedly prompt the user for input
while True:
    user_input = input("Please enter an English word to know its full meaning. Enter 'exit' to quit: ")
    if user_input == "exit":  # Check if the user wants to exit
        print("You are out of the operations. Please run again if you need more!")
        break  # Exit the loop
    else:
        print(translate(user_input), "\n")  # Call the translate function and print the result
    time.sleep(2)  # Pause for 1 second before the next iteration
