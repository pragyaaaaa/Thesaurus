import json
from difflib import SequenceMatcher, get_close_matches

# help(json.load)
data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        close_match = input("Did you mean %s ?" % get_close_matches(word, data.keys()))
        close_match = close_match.lower()
        if close_match == "yes" or close_match == "y":
            word_c = input("Okay! enter the correct word: ")
            return data[word_c]
    else:
        return "Word doesn't exist. Reconsider spell check."


word_user = input("Enter word: ")
print(translate(word_user))
