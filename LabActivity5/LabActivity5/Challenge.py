import nltk
from nltk.corpus import opinion_lexicon

try:
    happy_words = set(opinion_lexicon.positive())
    sad_words = set(opinion_lexicon.negative())
except LookupError:
    nltk.download("opinion_lexicon")
    happy_words = set(opinion_lexicon.positive())
    sad_words = set(opinion_lexicon.negative())


def number_happy(sentence):
    count = 0
    for word in sentence.lower().split():
        if word in happy_words:
            count += 1
    return count


def number_sad(sentence):
    count = 0
    for word in sentence.lower().split():
        if word in sad_words:
            count += 1
    return count


sentence = input("Enter a sentence: ")
happy = number_happy(sentence)
sad = number_sad(sentence)

print("Happy words:", happy)
print("Sad words:", sad)

if happy > sad:
    print("Tone: Happy (Positive)")
elif sad > happy:
    print("Tone: Sad (Negative)")
else:
    print("Tone: Neutral")