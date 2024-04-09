from replit import db
from datetime import datetime

def addTweet():
  tweet = input("What do you want to tweet? > ")
  timestamp = datetime.now()
  db[timestamp] = tweet

def viewTweet():
  keys = db.keys()
  tweet_list = list(keys)  # Convert keys to a list for easier manipulation
  tweet_list.reverse()  # Reverse the list to get most recent tweets first

  # Print 10 tweets at a time
  for i in range(0, len(tweet_list), 10):
      batch = tweet_list[i:i + 10]
      for key in batch:
          print(f"{key}: {db[key]}")
          print()

      next = input("Next 10 tweets? (y/n) > ")
      if next.lower() != "y":
          break

print("Tweeter")
while True:
  menu = input("1: Add Tweet\n2: View Tweets\n> ")
  if menu == "1":
    addTweet()
  elif menu == "2":
    viewTweet()
  else:
    print("Invalid input")

