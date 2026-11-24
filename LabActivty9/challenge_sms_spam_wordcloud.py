import re

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud

df = pd.read_csv("data/SMSSpamCollection", sep="\t", names=["label", "text"])

clean_text = []
for message in df["text"]:
    message = message.lower()
    message = re.sub(r"[^a-zA-Z]", " ", message)
    clean_text.append(message)

df["text"] = clean_text
stop_words = ["a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in", "is", "it", "of", "on", "or", "that", "the", "this", "to", "was", "we", "with", "you", "your"]

ham_text = " ".join(df.loc[df.label == "ham", "text"])
spam_text = " ".join(df.loc[df.label == "spam", "text"])

ham_cloud = WordCloud(width=800, height=800, background_color="white", stopwords=stop_words).generate(ham_text)
plt.figure(figsize=(8, 8))
plt.imshow(ham_cloud)
plt.title("Ham Messages")
plt.axis("off")
plt.savefig("output/ham_wordcloud.png")

spam_cloud = WordCloud(width=800, height=800, background_color="white", stopwords=stop_words).generate(spam_text)
plt.figure(figsize=(8, 8))
plt.imshow(spam_cloud)
plt.title("Spam Messages")
plt.axis("off")
plt.savefig("output/spam_wordcloud.png")

print("Ham word cloud saved to output/ham_wordcloud.png")
print("Spam word cloud saved to output/spam_wordcloud.png")
