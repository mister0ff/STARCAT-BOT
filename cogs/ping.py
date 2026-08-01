import discord
from discord.ext import commands
from discord import app_commands

# ===== VIEW COM BOTÃO =====
class PingView(discord.ui.View):
    def __init__(self, bot: commands.Bot):
        super().__init__(timeout=60)
        self.bot = bot

    @discord.ui.button(
        label="🔄 Atualizar ping",
        style=discord.ButtonStyle.primary
    )
    async def refresh(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        latency_ms = round(self.bot.latency * 1000)
        await interaction.response.edit_message(
            content=f"🏓 **Pong!** `{latency_ms}ms`",
            view=self
        )

# ===== COG =====
class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Mostra o ping do bot")
    async def ping(self, interaction: discord.Interaction):
        latency_ms = round(self.bot.latency * 1000)

        await interaction.response.send_message(
            content=f"🏓 **Pong!** `{latency_ms}ms`",
            view=PingView(self.bot),
          ephemeral=True
        )

# ===== SETUP =====
async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))
