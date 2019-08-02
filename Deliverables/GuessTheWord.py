import random
print("Welcome to our Guessing Game!")

# A list of words that 
potential_words = ["goldfish", "chicken", "falafel", "tortilla", "barbeque", "rainstorm", "donkey"]

word = random.choice(potential_words)

# Use to test your code:
# print(word)


# Converts the word to lowercase
word = word.lower()

print(word)

# Make it a list of letters for someone to guess
current_word = [] # TIP: the number of letters should match the word

# for each letter in chosen word, generates a dash

for letter in word:
    current_word.append("_")

print(current_word)

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
    guess = input("Guess a letter: ")
    if guess not in letters: # check if the guess is valid: Is it one letter? Have they already guessed it?
        print("Try again. Guess one letter this time!")
    elif guess not in word:
        fails = fails + 1
        print("Try again. This letter is not in the word!")
        print("You have " + str(maxfails - fails) + " tries left!")
    elif guess in word:
        for i in range(0, len(word)):
            if word[i] == guess:
                current_word[i] = guess
                print(current_word)
        fails = fails
    if "_" not in current_word:
        print("You win!")
        break

while fails >= maxfails:
    print("You're out of tries! Game over! :( The word was", word)
    break
        


	# check if the guess is correct: Is it in the word? If so, reveal the letters!




