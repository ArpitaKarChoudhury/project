# Initialize dictionaries for Birds, Reptiles, and Insects with animal hints
Birds = {
    'Parrot': "I am green in color and have a reddish beak",
    'Peacock': "I am colorful and known as the national bird of India",
    'Hen': "I am a domestic bird and give you eggs for omelette"
}

Reptiles = {
    'Crocodile': "I am brownish green in color, big in size, and live in water",
    'Snake': "I make a hiss sound and can move without any legs"
}

Insects = {
    'Butterfly': "I have colorful wings and undergo metamorphosis",
    'Ant': "I am a tiny creature and live in colonies"
}

# Initialize a dictionary 'categories' to map category keys to the corresponding animal dictionaries
categories = {'R': Reptiles, 'B': Birds, 'I': Insects}

# Prompt the user for their name
name = input("Please enter your name: ")
print(f"Hi {name}, Welcome to the advanced animal guessing game.")

# Prompt the user to choose a category
print("Choose one of the below categories by entering the first letter in capitals: Reptiles, Birds, Insects")
user_input = input()


# Fetch the appropriate dictionary based on the user's choice
chosen_category = categories.get(user_input)

if chosen_category is None:
    print("Invalid category. Please choose from Reptiles, Birds, or Insects.")
else:
    for animal, hint in chosen_category.items():
        print(f"Hints: {hint}")
        attempts = 1

        while attempts >= 0:
            guess = input("What is your guess? ")
           

            if guess == animal:
                print("Excellent. You are right.")
                break
            else:
                if attempts > 0:
                    print(f"Incorrect! Please try again. You have {attempts} more attempt(s).")
                    attempts -= 1
                else:
                    print(f"Sorry, you have exhausted all attempts. The correct answer was {animal}.")
abc = input("y/n")

           
print("Thanks for playing!")
