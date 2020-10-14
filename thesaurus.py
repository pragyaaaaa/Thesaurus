import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))
data_synonyms = json.load(open("eng_synonyms.json"))


def translate_synonyms(word):
    word = word.lower()
    if word in data_synonyms:
        return data_synonyms[word]
    else:
        return "Word doesn't exist. Reconsider spell check."


def translate(word):
    global right_word
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        close_match = input("Did you mean %s ? Enter (Y/yes) for affirmative. " % get_close_matches(word, data.keys()))
        close_match = close_match.lower()
        if close_match == "yes" or close_match == "y":
            word = input("Okay! enter the correct word: ")
            right_word = word
            return data[word]
        else:
            return "Word doesn't exist. Reconsider spell check."
    else:
        return "Word doesn't exist. Reconsider spell check."


def output(out):
    if type(out) == list:
        for element in out:
            print(element)
    else:
        print(out)


def input_u():
    word_user = input("Enter word: ")
    result = translate(word_user)
    output(result)
    synonyms = input("Satisfied? Or wanna go deeper?: (y/n): ")
    if synonyms == "yes" or synonyms == "y":
        result = translate_synonyms(right_word)
        output(result)
    elif synonyms == "no" or synonyms == "n":
        loop = input("Wanna try again?(Y/n): ")
        if loop == "yes" or loop == "y":
            word_user = input("Enter word: ")
            result = translate(word_user)
            output(result)
        else:
            print("Thank you! try again sometime.")
    return


input_u()
