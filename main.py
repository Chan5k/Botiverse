import discord
from discord.ext import commands
import openai

# Define your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Define bot prefix and create an instance of the bot
bot_prefix = "!"
bot = commands.Bot(command_prefix=bot_prefix)

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user.name}')

# Define a command for AI chat
@bot.command()
async def chat(ctx, *, question):
    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        max_tokens=50  # You can adjust the response length as needed
    )

    # Send the AI-generated response to the user
    await ctx.send(response.choices[0].text)

# Run the bot with your token
bot.run("YOUR_BOT_TOKEN")
