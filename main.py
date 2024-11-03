import os 
import disnake as discord
from disnake.ext import commands 
from json import load 


# config
with open("config/config.json", "r") as config:
	file = load(config)

token = file["token"]
prefix = file["prefix"]

client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), case_insensitive=True)

@client.event 
async def on_ready():
	print(f"Bot >>>>> {client.user} <<<<< Iniciado com sucesso!")

def load_commands(folder):
	for folders in os.listdir(folder):
		for files in os.listdir(f"{folder}/{folders}"):
			if files.endswith(".py"):
				Dir = f"{folder}.{folders}.{files}"
				client.load_extension(Dir[:-3])

if __name__ == "__main__":
	load_commands("commands")
	client.run(token)