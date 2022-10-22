import random
import time
from replit import clear
from Hangman_stages import stages


# 1. enlarging list of words & random choice
word_list = open('words').read().split("\n")
word = random.choice(word_list)

# 2. hiding letters for the user output
hidden_word = []
for i in range(len(word)):
    hidden_word += "_"

print("Guess the word!\n")
print(" ".join(hidden_word))

time.sleep(0.5)

death = 6
# 3. Adding while loop to repeat adding letter as many times as it is possible
while "_" in hidden_word and death != 0:
    user_letter = input("Choose the letter: ").lower()

    # 3.1. are you using that letter again?!
    if user_letter in hidden_word:
        print("You already used this letter.")

    # 3.2. Compare the user_letter to the letter in word and its position
    for position in range(len(word)):

        # now we need to compare position to the letter
        # and replace the index of the position in hidden_word with the user_letter/letter
        letter = word[position]
        if user_letter == letter:
            hidden_word[position] = letter



    # 3.3. Adding the other possibility and death visualization
    if user_letter not in word:
        clear()
        death -= 1
        print(f"This letter - {user_letter} - is not in the word. You lose a life.")
        print(stages[death])
    print(" ".join(hidden_word))


if death == 0:
    print(f"You lost. The word was:\033[1m {word} \033[0m")
else:
    print("you won")
