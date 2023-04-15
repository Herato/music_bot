from logging import Logger
from app.main import client

logger = Logger("volume")


@client.command(name="volume")
async def volume(ctx, vol: int):
    if ctx.voice_client is None:
        return await ctx.send("Nie jestem połączony z żadnym kanałem głosowym.")

    if not 0 < vol < 101:
        return await ctx.send("Głośność musi być ustawiona w przedziale od 1 do 100.")

    ctx.voice_client.source.volume = vol / 100
    await ctx.send(f"Głośność muzyki ustawiona na {vol}%.")


async def setup(bot):
    bot.add_command(volume)
    logger.info("Setup done.")