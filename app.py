import json
import urllib.request
import emoji

# retrieve the EmojiNet data from the GitHub repository
url = 'https://raw.githubusercontent.com/uclnlp/EmojiNet/master/EmojiNet.json'
response = urllib.request.urlopen(url)
data = json.loads(response.read())

# ask the user to input an emoji
emoji_input = input("Enter an emoji: ")

# normalize the input to Unicode character format
emoji_input = emoji.demojize(emoji_input)
emoji_input = emoji_input.replace("_", " ")

# find the meaning of the input emoji in the EmojiNet data
for emoji in data:
    if emoji["emoji"] == emoji_input:
        print("The meaning of the emoji", emoji_input, "is", emoji["meanings"])
        break
else:
    print("Invalid emoji")
