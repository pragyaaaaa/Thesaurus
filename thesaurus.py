import json

# help(json.load)
data = json.load(open("data.json"))


def translate(word):
    return data[word]


word_user = input("Enter word: ")
print(translate(word_user))
