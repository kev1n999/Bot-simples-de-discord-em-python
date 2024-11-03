import sqlite3 as sql 
from json import load


with open("config/config.json", "r") as config:
	file = load(config)

prefix = file["prefix"]

class Database:
    def __init__(self):
        self.c = sql.connect("database/prefixes.db")
        self.cursor = self.c.cursor()

    def prefixes(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS prefixos (prefix TEXT, guild_id INTEGER)")
        

    def get_prefix(self, bot, message):
        Id = message.guild.id 
        self.cursor.execute(f"SELECT prefix FROM prefixos WHERE guild_id = ?", (Id,))
        p = self.cursor.fetchone()
        return p[0] if p else prefix
    