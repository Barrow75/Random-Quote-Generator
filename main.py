# Generate a random quote based on the users output
import random
import json

print("Welcome To The Quote Generator!")
print("Choose A Random Quote From Any Of The People Below:")
print("- Walt Disney")
print("- Babe Ruth")
print("- Tony Stark")
print("- Joker")
print("- Ultron")
print("- Fernando Vera")
print("- Elliot Alderson")
print("---------------------------------------------------------------")

AnotherQuote ="y"
while AnotherQuote == "y":

    with open("Quotes.json") as file:
        data = json.load(file)

    user = input("Who would you like a quote from? ")
    if user in data:
        quotes = data[user]
        random_quote = random.choice(quotes)
        print(f"{random_quote} -{user}")
    else:
        print(f"Sorry {user} is not one of the options")

    AnotherQuote = input("Would you like another quote?: ")
    if AnotherQuote == "n":
        print("Goodbye")
        break
