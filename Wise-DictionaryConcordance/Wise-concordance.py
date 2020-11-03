# Nick Wise
# 10/27/2020

# NOTES: Program currently has only been tested with 1 file.
# TODO: add validation check for file input, user entered word.

# This program will:
# ask a user to enter a file/files.
# ask user for word to look up in file.
# find word and convert it to uppercase and print total occurrences
# for each occurrence. Print line number and local context.

# function to read file and something else
import os


def main():
    concordance = {}
    files = get_files()

    for file in files:
        contents = read_files(file)
        # removes extension to be placed as proper key in dictionary
        title = os.path.splitext(file)[0]
        # makes dictionary with title and content of file
        concordance[title] = contents
        # converting list to lowercase to analyse in remove stop words
        lower_list = [word.lower() for word in contents]
        # reads and removes stop words from file.
        updated_contents = remove_stop_words(lower_list)
        # gets user input for word to search
        word = get_user_word()
        # counts occurrences
        occurrences = count_occurrence(word, updated_contents)
        bolded_user_word = uppercase_occurrences(word, contents)
        # print(bolded_user_word) # this is for testing
        line_of_word = find_line(word, bolded_user_word)
        # Display information back to user
        display_info(word, occurrences, line_of_word, bolded_user_word)


def get_files():
    # file = 'itsy_bitsy_spider.txt'
    files = []
    # set flag so user can enter manly different files.
    more_files = True
    while more_files:
        file = input("Please enter file path.\nNote: press the enter key when you are done inputting your files.\n")
        files.append(file)
        # if user pressed enter key, delete '' entry and return files
        if file == '':
            files.pop()

            return files


# function to read files and place them in list.
def read_files(file):
    with open(file, 'r') as f:
        all_lines = f.readlines()
        return all_lines


# removes stop words from files
def remove_stop_words(contents):
    stop_words = "english_stop.txt"
    with open(stop_words, 'r') as w:
        lines = w.readlines()
        # strips stop word file of new line character
        lines = [i.strip() for i in lines]
        # strips file content of new line character
        contents = [i.strip() for i in contents]
        # makes list of words from contents of file
        split_words = [i for item in contents for i in item.split()]
        # makes a new list comparing the list of stop words to list of words in file content
        content_without_stop_words = [i for i in split_words if i not in lines]

        return content_without_stop_words


# Function to get a word from user
def get_user_word():
    word = input("Please enter word to look for in your files.\n")

    return word


# Function to count occurrences
def count_occurrence(word, contents):
    if word in contents:
        count = contents.count(word)
        return count


def uppercase_occurrences(word, contents):
    # will strip the new line character off file contents
    # contents = [i.strip() for i in contents]

    # sets up variables to compare user word to the word in contents of file.
    exact_word = f" {word} "
    title_case_word = f" {word.title()} "
    lowercase_word = f" {word.lower()} "
    upper_word = f"{word.upper()}"

    # iterates over the lines in file contents and if it matches our local variables
    for line in contents:
        if exact_word in line:
            # replace every word in contents that matches exact word to uppercase word and return the value
            make_uppercase = [sub.replace(word, upper_word) for sub in contents]
            return make_uppercase
        elif title_case_word in line:
            # replace every word in contents that matches exact word to uppercase word and return the value
            make_uppercase = [sub.replace(word.title(), upper_word) for sub in contents]
            return make_uppercase
        elif lowercase_word in line:
            # replace every word in contents that matches exact word to uppercase word and return the value
            make_uppercase = [sub.replace(word.lower(), upper_word) for sub in contents]
            return make_uppercase


# Function for finding and indexing the users word.
def find_line(user_word, bolded_user_word):
    lines_that_contain_word = []
    upper = user_word.upper()
    # stores each sentence as a list inside another list.
    split_sentence = [[item] for item in bolded_user_word]
    # iterates over lists within a list to find line that word occurred
    for i in split_sentence:
        for e in i:
            if upper in e:
                # finds the index of the sentence words appears in and
                # stores those values in an empty list to be returned
                line_of_word = split_sentence.index(i)
                lines_that_contain_word.append(line_of_word)

    return lines_that_contain_word


# function to display user word, occurrences, the line number the word appears on and the line itself.
def display_info(word, occurrences, line_of_word, bolded_user_word):
    message = f"{word}: Total Count:{occurrences}\n"
    print(message)
    for line in line_of_word:
        split_sentence = [item for item in bolded_user_word]
        print(f"\tLine {line + 1}: {split_sentence[line]}")


main()
