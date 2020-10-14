import json

# help(json.load)
data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "Word doesn't exist. Reconsider spell check."


word_user = input("Enter word: ")
print(translate(word_user))
