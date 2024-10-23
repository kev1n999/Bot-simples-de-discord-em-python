import os
import disnake as discord
from disnake.ext import commands
from json import load

with open("config/config.json", "r") as config:
    l = load(config)

token = l["token"]
prefix = l["prefix"]

client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f"O bot >>> {client.user} <<< foi iniciado com sucesso!")

def load_commands(folder):
    for folders in os.listdir(folder):
        for files in os.listdir(f"{folder}/{folders}"):
            if files.endswith(".py"):
                Commands = files[:-3]
                client.load_extension(f"{folder}.{folders}.{Commands}")
                print(Commands)

if __name__ == "__main__":
    load_commands("commands")
    client.run(token)