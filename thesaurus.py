import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))
data_synonyms = json.load(open("eng_synonyms.json"))


def translate_synonyms(word):
    word = word.lower()
    if word in data_synonyms:
        return data_synonyms[word]
    elif len(get_close_matches(word, data_synonyms.keys())) > 0:
        close_match = input(
            "Did you mean %s ? Enter (Y/yes) for affirmative. " % get_close_matches(word, data_synonyms.keys()))
        close_match = close_match.lower()
        if close_match == "yes" or close_match == "y":
            word_c = input("Okay! enter the correct word: ")
            return data_synonyms[word_c]
        else:
            return "Word doesn't exist. Reconsider spell check."
    else:
        return "Word doesn't exist. Reconsider spell check."


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        close_match = input("Did you mean %s ? Enter (Y/yes) for affirmative. " % get_close_matches(word, data.keys()))
        close_match = close_match.lower()
        if close_match == "yes" or close_match == "y":
            word_c = input("Okay! enter the correct word: ")
            return data[word_c]
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
        result = translate_synonyms(word_user)
        output(result)
    elif synonyms == "no" or synonyms == "n":
        loop = input("Wanna try again?(Y/n): ")
        if loop == "yes" or loop == "y":
            word_user = input("Enter word: ")
            result = translate_synonyms(word_user)
            output(result)
        else:
            print("Thankyou! Try again.")
    return


input_u()
