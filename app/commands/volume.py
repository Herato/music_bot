from logging import Logger
from app.main import client

logger = Logger("volume")


@client.command(name="volume")
async def _volume(self, ctx: commands.Context, *, volume: int):
        """Sets the volume of the player."""

    if not ctx.voice_state.is_playing:
        return await ctx.send('Nothing being played at the moment.')

    if 0 > volume > 100:
        return await ctx.send('Volume must be between 0 and 100')

    ctx.voice_state.volume = volume / 100
    await ctx.send('Volume of the player set to {}%'.format(volume))


async def setup(bot):
    bot.add_command(volume)
    logger.info("Setup done.")