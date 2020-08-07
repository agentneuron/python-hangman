import os
import random
import sys

wordlist = []


def display_menu():
    menu_items = ['\n', '_', '1. Play Game', '2. Display Dictionary Stats', '3. Exit Game', '-']
    for x in menu_items:
        print(x)
    menu_select = input("\nmake a Choice --> ")[0]
    if menu_select == "1":
        play_game(random.choice(wordlist))
    elif menu_select == "2":
        word_stats()
    elif menu_select == "3":
        print("goodbye!")
        sys.exit()
    else:
        print("nope! good bye!")


def create_list():
    wordfile = open("words.txt", "r", encoding="utf-8")
    lines = wordfile.readlines()
    for count in range(0, len(lines) - 1):
        x = lines[count]
        wordlen = len(x)
        a = x[:wordlen - 1]
        if (wordlen <= 13) and (wordlen >= 7):
            wordlist.append(a)
    wordlist.append(lines[count + 1])
    wordfile.close()


def word_stats():
    longest_word = ''
    longest_word_length = 1
    shortest_word_length = 1
    shortest_word = wordlist[1]
    palindromes = []
    for the_word in wordlist:
        if len(the_word) > longest_word_length:
            longest_word = the_word
            longest_word_length = len(longest_word)
        if (len(the_word)) < len(shortest_word):
            shortest_word = the_word
            shortest_word_length = len(the_word)
        if the_word[::-1] == the_word:
            palindromes.append(the_word)
    print("Dictionary statistics:")
    print(f"\ttotal available words : {len(wordlist)}")
    print(f"\tlongest word : {longest_word} ({longest_word_length})")
    print(f"\tshortest word : {shortest_word} ({shortest_word_length})")
    print(f"\tpalindromes :  {len(palindromes)} - {palindromes}")
    display_menu()

def check_word(fake_word, word):
    eval_word = ''.join(fake_word)
    if eval_word == word:
        print("Good job! You WIN!!")
        return True


def setup():
    if os.path.isfile("words.txt"):
        create_list()
        if (len(wordlist)) < 10:
            print("Word list too small, add words to make game challenging!")
            print("")
            sys.exit()
    else:
        print("words.txt file not found.  this file should be placed in the same directory as the main .py file")
        sys.exit()


def play_game(word):
    attempts = 5
    index = 0
    in_word = False
    solved = False
    guesses = []
    fake_word = []
    bad_chars = "`~!@#$%^&*()_+-= |:;0123456789"
    for x in word:
        fake_word += "_"
    print(f"Word length for this game : {len(word)}")
    print(f"Incorrect attempts permitted :  : {attempts}")
    while attempts > 0 and solved is not True:
        guess = input("Enter a letter : ")[0].lower()
        if guess in bad_chars:
            print("Letter cannot be a #, symbol or empty input - try again!")
        elif guess in guesses:
            print("You've already guessed that letter. Try again")
        else:
            guesses.append(guess)
            for count in word:
                index += 1
                if guess == count:
                    fake_word[index - 1] = count
                    in_word = True
            if not in_word:
                attempts -= 1
                if attempts != 0:
                    print(f"Nope - try again - {attempts} tries remaining")
            else:
                in_word = False
            index = 0
            print(f"word : {''.join(fake_word)}")
            print(f"guesses : {','.join(guesses)} - {attempts} remaining")
            solved = check_word(fake_word, word)
            if solved:
                print("Wowzers! You Won!")
            if attempts == 0:
                print(f"You lose! the word was {word}")


def main():
    setup()
    display_menu()


if __name__ == "__main__":
    main()
