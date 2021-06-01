import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def find_word(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title in data:
        return data.title[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("Do you mean %s instead " %get_close_matches(word , data.keys())[0])
        option = input("Press y for yes n for no ")
        if option == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif option == "n":
            return "Could not find the word, check it again"
        else:
            return "Please choose n or y "

    else:
        print("Could not find the word, check it again")

word = input("Enter Word to search meaning: ")
meaning = find_word(word)
if type(meaning) == list:
    for item in meaning:
        print(item)
else:
    print(meaning)
