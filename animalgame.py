# Define a dictionary for each category with animals and their hints
categories = {
    "Reptiles": {
        "Crocodile": "I am brownish green in colour, big in size and live in water.",
        "Snake": "I make a hiss sound and can move without any legs."
    },
    "Birds": {
        "Eagle": "I have a sharp beak and excellent vision.",
        "Penguin": "I am a flightless bird and live in cold regions."
    },
    "Insects": {
        "Butterfly": "I have colorful wings and undergo metamorphosis.",
        "Ant": "I am a tiny creature and live in colonies."
    }
}

def play_game():
    name = input("Please enter your name: ")
    print(f"Hi {name}, Welcome to the advanced animal guessing game.")
    
    # Ask the user to choose a category
    print("Choose one of the below categories by entering the first letter in capitals: Reptiles, Birds, Insects")
    category = input()
    category = category.strip()
    
    if category not in categories:
        print("Invalid category. Please choose from Reptiles, Birds, or Insects.")
        return

    print(f"Great! You have chosen the {category} category. Now, I will give you some hints and you can try to guess the animals.")
    
    animals = categories[category]
    
    for animal, hint in animals.items():
        print(f"Hints: {hint}")
        attempts = 2
        
        while attempts >= 0:
            guess = input("What is your guess? ")
            guess = guess.strip()
            
            if guess == animal:
                print("Excellent. You are right.")
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Incorrect! Please try again. You have {attempts} more attempt(s).")
                else:
                    print(f"Sorry, you have exhausted all attempts. The correct answer was {animal}.")
    
    print("Thanks for playing!")

if __name__ == "__main__":

    while True:
        play_game()
        abc= input("Y/N")
        if "N" == abc:
            break
