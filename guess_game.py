guess_word = "Love"
guess = ""
guess_count = 0
guess_limit = 3
print("Welcome!!")
print("You have three chances to guess the correct word.\nGood Luck!!")
print("You have the following list of words to choose from: ")
print(" Mine\n", "Queen\n", "King\n", "Princess\n", "Love\n", "Zebra\n", "Elephant\n")
while guess != guess_word and guess_count != guess_limit:

    guess = input("Enter your guess word: ")
    if guess_word != guess:
        print("Sorry " + guess + " is not the correct word\nTry again.")
        guess_count += 1

if guess == guess_word:
    print("Congratulations,"+guess+ " is the correct word\nYou Win!")
else:
    print("You have exhausted your guess limit, You Lose!")