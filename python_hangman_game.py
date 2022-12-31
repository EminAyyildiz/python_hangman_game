#Written by Emin Ayyıldız

print,("Written by Emin Ayyıldız GOOD GAMEEEE.... :)) ")

word = input("Please enter a word : ")

guesses_left = int(input("How many times are you allowed to make mistakes? :"))

guessed_character = []
press = []
correct_guesses = []

for character in word:
    correct_guesses.append("_")

while guesses_left > 0:
    
    print(" ".join(correct_guesses))
    print(f"Your remaining guess: {guesses_left}")
    guess = input("Guess a letter:")

    if guess in guessed_character:
        print("You already guessed this letter!")
        print(f"Your remaining guess: {guesses_left}")
        continue

    elif guess in word:
        print("Correct Guess")
        print(f"Your remaining guess: {guesses_left}")
        for emin in range(len(word)):
            if word[emin] == guess:
                correct_guesses[emin] = guess

    else:
        print("Wrong Guess!")
        guesses_left -= 1
    guessed_character.append(guess)
    if "_" not in correct_guesses:
        print(" ".join(correct_guesses))
        print("Congratulations, you found the word!")
        break
if guesses_left == 0:
    print("Sorry, you've run out of guesses. Correct answer:", word)
