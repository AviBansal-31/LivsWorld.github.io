#import JSON library
import json

#Open JSON file
tweetFile = open("./twitter.json", "r")

#get tweetData
tweetData = json.load(tweetFile)

#close file after storing data
tweetFile.close()

print(tweetData[1]["user"]["description"])

for i in range(len(tweetData)):
    print("Tweet text:" + tweetData[i]["text"])
