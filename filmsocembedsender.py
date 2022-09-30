# Libraries
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load .env, set the TOKEN
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
#intents.messages = True


bot = commands.Bot(command_prefix='!f', description='Big Chungus', intents=intents)




@bot.command()
async def embed(ctx):
    # Current embed created using: https://cog-creators.github.io/discord-embed-sandbox/

    # Rules Channel
    # channel = bot.get_channel(1024723112044019752)

    # Announcements Channel
    # channel = bot.get_channel(899729762656849945)

    # bot-stuff channel: for testing
    # channel = bot.get_channel(1024807754784833616)



    embed=discord.Embed (title='Server Info', description='Included below is a brief list of our server rules. If you have any queries about specific rules / if something is unclear, feel free to message a member of the committee', color=discord.Color.random())
    embed.set_author(name="Galway Film Society", url="https://discord.gg/tNE83FGY8x", icon_url="https://images-ext-1.discordapp.net/external/X3jP4tDGT1oEBTfJXxlCgjWgMYeBjs1vn6nI5suwsjU/https/cdn.discordapp.com/icons/899729762656849940/dc854c6f0d4588177941e19970f3effb.webp")
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/X3jP4tDGT1oEBTfJXxlCgjWgMYeBjs1vn6nI5suwsjU/https/cdn.discordapp.com/icons/899729762656849940/dc854c6f0d4588177941e19970f3effb.webp")
    embed.add_field(name="Rules", value="This is like George Orwell's film, 1984(1984)", inline=False)
    embed.add_field(name="#1", value="No blank nicknames; no inappropriate nicknames or profile pictures", inline=True)
    embed.add_field(name="#2", value="Discrimination of any kind will not be tolerated on this server. Anyone found to be engaging in some form of harassment, degradation or discrimination will be kicked from the server.", inline=False)
    embed.add_field(name="#3", value="Strictly no NSFW", inline=True)
    embed.add_field(name="#4", value="Your student ID needs to be sent to one of the committee members ", inline=True)
    embed.add_field(name="(This is not an exhaustive list, and may be added to in the future.)", value="If you have any concerns or complaints, or if you are feeling uncomfortable please reach out to a committee member, we are happy to help with any worries you may have.", inline=False)
    embed.add_field(name="Other Stuff", value="Make sure to send a Committee member your Student ID so we can add you as a member! You can set your year and pronouns in the  [roles and pronouns](https://discord.com/channels/899729762656849940/1024717472353501254) channel, and your display colour in the [colour](https://discord.com/channels/899729762656849940/1024745432536072202) channel.", inline=True)
    embed.set_footer(text="Official Galway Film Soc Missive")
   # embed.set_image(url="https://images-ext-1.discordapp.net/external/X3jP4tDGT1oEBTfJXxlCgjWgMYeBjs1vn6nI5suwsjU/https/cdn.discordapp.com/icons/899729762656849940/dc854c6f0d4588177941e19970f3effb.webp")    


   
    await channel.send(embed=embed)



bot.run(TOKEN)
