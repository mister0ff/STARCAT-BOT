import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise RuntimeError("TOKEN não encontrado no .env")

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
# 🔹 ADICIONADO: Necessário para o bot ler as mensagens e responder ao nome dele
intents.message_content = True 

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="$",
            intents=intents
        )

    async def setup_hook(self):
        # 🔹 AUTO-LOAD DE TODOS OS COGS
        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                await self.load_extension(f"cogs.{file[:-3]}")

        # 🔹 SYNC GLOBAL (bot público)
        await self.tree.sync()
        print("🌍 Slash commands sincronizados")
        print("✅ Todos os cogs carregados")

bot = MyBot()

@bot.event
async def on_ready():
    print(f"🛸StarCat On: {bot.user}")

bot.run(TOKEN)
