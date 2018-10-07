import json
import pandas as pd
import matplotlib.pyplot as plt
import re
 
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False
 
 
tweets_data_path = 'twitter_data.txt'
 
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
tweets_file.close()
 
print len(tweets_data)
 
tweets = pd.DataFrame()
 
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
 
tweets_by_lang = tweets['lang'].value_counts()
 
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=7)
ax.tick_params(axis='y', labelsize=7)
ax.set_xlabel('Languages', fontsize=7)
ax.set_ylabel('Number of tweets' , fontsize=7)
ax.set_title('Top Used terms', fontsize=9, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
 
tweets['manutd'] = tweets['text'].apply(lambda tweet: word_in_text('manutd', tweet))
tweets['barca'] = tweets['text'].apply(lambda tweet: word_in_text('barca', tweet))
 
print tweets['manutd'].value_counts()[True]
print tweets['barca'].value_counts()[True]
 
prg_langs = ['manutd', 'barca']
tweets_by_prg_lang = [tweets['manutd'].value_counts()[True], tweets['barca'].value_counts()[True]]
 
x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')
 
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: Manchester United vs Barcelona(Raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.grid()
 
fig.show()