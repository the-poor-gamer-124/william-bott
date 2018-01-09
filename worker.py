import discord
import random
import pickle
import time
import os

client = discord.Client()
Token = str(os.environ.get('Token'))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



@client.event
async def on_message(message):
    start = time.time()
    if message.author == client.user:
        return
    if message.content.startswith("HELP"):
        print("Help: " + str(message.channel))
        await client.send_message(message.channel, "\"line\" for Pick-up Line (PG-13)")
        await client.send_message(message.channel, "\"joke\" for Funny Joke to tell (NA)")
        client.logout()
    if message.content.startswith("test"):
        print("Test: " + str(message.channel))
        await client.send_message(message.channel, "Hello William")
        client.logout()
    if message.content.startswith("Test"):
        print("Test: " + str(message.channel))
        await client.send_message(message.channel, "Hello William")
        client.logout()
    if message.content.startswith("line"):
        print("Line: " + str(message.channel))
        pickle_in = open("pickup.pickle", "rb")
        example = pickle.load(pickle_in)
        randomQuote = random.randint(1, 22)
        await client.send_message(message.channel, example[randomQuote])
        client.logout()
    if message.content.startswith("Line"):
        print("Line: " + str(message.channel))
        pickle_in = open("pickup.pickle", "rb")
        example = pickle.load(pickle_in)
        randomQuote = random.randint(1, 22)
        await client.send_message(message.channel, example[randomQuote])
        client.logout()
    if message.content.startswith("joke"):
        print("Joke: " + str(message.channel))
        pickle_in = open("joke.pickle", "rb")
        example = pickle.load(pickle_in)
        randomJoke = random.randint(1, 10)
        await client.send_message(message.channel, example[randomJoke])
        client.logout()
    if message.content.startswith("Joke"):
        print("Joke: " + str(message.channel))
        pickle_in = open("joke.pickle", "rb")
        example = pickle.load(pickle_in)
        randomJoke = random.randint(1, 10)
        await client.send_message(message.channel, example[randomJoke])
        client.logout()
    if message.content.startswith("ping"):
        print("Ping: " + str(message.channel))
        await client.send_message(message.channel, "Pong!")
        end = time.time()
        total = end - start
        await client.send_message(message.channel, "Time: " + str(total) + " Seconds")
        if total < 0.06:
            await client.send_message(message.channel, "Great Connection")
        elif 1 > total > 0.06:
            await client.send_message(message.channel, "Okay Connection")
        else:
            await client.send_message(message.channel, "Bad Connection")
        client.logout()
    if message.content.startswith("Ping"):
        print("Ping: " + str(message.channel))
        await client.send_message(message.channel, "Pong!")
        end = time.time()
        total = end - start
        await client.send_message(message.channel, "Time: " + str(total) + " Seconds")
        if total < 0.06:
            await client.send_message(message.channel, "Great Connection")
        elif 1 > total > 0.06:
            await client.send_message(message.channel, "Okay Connection")
        else:
            await client.send_message(message.channel, "Bad Connection")
        client.logout()
    if message.content.startswith("Secret"):
        print("Secret: " + str(message.channel))
        pickle_in = open("secret.pickle", "rb")
        example = pickle.load(pickle_in)
        randomJoke = random.randint(1, 10)
        await client.send_message(message.channel, example[randomJoke])
        client.logout()
    if message.content.startswith("secret"):
        print("Secret: " + str(message.channel))
        pickle_in = open("secret.pickle", "rb")
        example = pickle.load(pickle_in)
        randomJoke = random.randint(1, 10)
        await client.send_message(message.channel, example[randomJoke])
        client.logout()

client.run(Token)

