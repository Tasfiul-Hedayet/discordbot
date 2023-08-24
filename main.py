import discord
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

intents = discord.Intents.default()
client = discord.Client(intents=intents)
# Define your responses for different moods
happy_responses = ["I'm glad to hear that!", "That's fantastic!", "Happiness is wonderful!"]
sad_responses = ["I'm here for you.", "It's okay to feel down sometimes.", "Sending virtual hugs."]
emotional_responses = ["Emotions are a complex thing.", "Feelings can be quite powerful.", "Take a deep breath and reflect on your emotions."]

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    # Check for different mood keywords and respond accordingly
    if any(word in msg for word in ["happy", "joy", "excited"]):
        response = random.choice(happy_responses)
        await message.channel.send(response)
    elif any(word in msg for word in ["sad", "down", "unhappy"]):
        response = random.choice(sad_responses)
        await message.channel.send(response)
    elif any(word in msg for word in ["emotional", "feelings"]):
        response = random.choice(emotional_responses)
        await message.channel.send(response)

# Replace "YOUR_BOT_TOKEN" with your actual bot token
client.run(os.getenv("TOKEN"))