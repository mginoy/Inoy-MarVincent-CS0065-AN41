import re

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud

df = pd.read_csv("data/emails.csv")

print("Spam count:", len(df.loc[df.spam == 1]))
print("Not spam count:", len(df.loc[df.spam == 0]))
print("Original shape:", df.shape)

df["spam"] = df["spam"].astype(int)
df = df.drop_duplicates()
df = df.reset_index(drop=True)[["text", "spam"]]

print("Shape after removing duplicates:", df.shape)

clean_desc = []
for w in range(len(df.text)):
    desc = df["text"][w].lower()
    desc = re.sub(r"[^a-zA-Z]", " ", desc)
    desc = re.sub(r"&lt;/? .*?&gt;", " ", desc)
    desc = re.sub(r"(\d|\W)+", " ", desc)
    clean_desc.append(desc)

df["text"] = clean_desc

stop_words = ["is", "you", "your", "and", "the", "to", "from", "or", "i", "for", "do", "get", "not", "here", "in", "im", "have", "on", "re", "new", "subject"]

wordcloud = WordCloud(
    width=800,
    height=800,
    background_color="black",
    stopwords=stop_words,
    max_words=1000,
    min_font_size=20,
).generate(str(df["text"]))

plt.figure(figsize=(8, 8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("output/all_email_wordcloud.png")

print("Word cloud saved to output/all_email_wordcloud.png")
