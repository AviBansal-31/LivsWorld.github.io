import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("./twitter.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

#create list for polarity and subjectivity
polarityList = []
subjectivityList = []

#from each tweet make a textblob from text
#use a for loop
for tweet in tweetData:
    tweetblob = TextBlob(tweet["text"])
    #store each tweet's polarity and subjectivity in respective lists
    polarityList.append(tweetblob.polarity)
    subjectivityList.append(tweetblob.subjectivity)

print(polarityList)
print(subjectivityList)

#now make a histogram

plt.hist(polarityList, bins=[-1.1, -.75, -.5, -.25, 0, .25, .5, .75, 1.1], facecolor = (.55, .6, .7))
plt.xlabel("Polarity")
plt.ylabel("Number of Tweets")
plt.title("Polarity of Tweets")
plt.axis([-1, 1, 0, len(polarityList)])
plt.grid(False)
plt.show()

#how to make wordcloud
tweetstring = ""
for i in range(len(tweetData)):
    tweetstring += str(tweetData[i]["text"])

tb = TextBlob(tweetstring)
wordstoFilter = ["http", "and", "in", "the", "about", "to", "of", "at"]
filteredDictionary = dict()
    
