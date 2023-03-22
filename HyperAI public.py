from ctypes import FormatError
import os
import openai
import random
import logging
import discord
import time
from discord.ext import commands
from asyncio import sleep
import asyncio
import colorama
from colorama import Fore
colorama.init()

#clients
client = discord.Client()
client = commands.Bot(command_prefix="!")
openai.api_key = ''
logging.basicConfig(filename="log.txt", level=logging.INFO,
                    format="%(asctime)s %(message)s")

#on ready
@client.event
async def on_ready():
    activity = discord.Game(name="HyperAI", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)

#backmovement
async def backmovement():
    back = asyncio.create_task(on_message())
    await back

#bot
@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Use GPT-3 to generate a response to the user's message
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message.content}\n",
        max_tokens=200,
        temperature=1,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    ).choices[0].text
    print(f'{Fore.BLUE}Author: {message.author}')
    print(f'{Fore.CYAN}Message: {message.content}')
    print(f'{Fore.GREEN}Response: {response}{Fore.RESET}')
    logging.info(f" Author = {message.author} ; Message: {message.content} ; Response: {response}")
    print('')

    await message.channel.send(response)
    
client.run('')
