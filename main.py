import discord
import asyncio
import os

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
token = "BOT-TOKEN-HERE"
client = discord.Client(intents=intents)
role_id = 00000000000000 #Replace with your own role-id
delay_between_pings = 0.0

target_channel_ids = [
    0000000000000000001, #Replace with your channel-id
    0000000000000000002, #Replace with your channel-id
    #More can be added
]

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Zenith Pinger v0.1", url="https://twitch.tv/zensware"))
    os.system('clear')
    print(f"{client.user} - Zenith is now hosting!")
    while True:
        await spam_channels_with_ping(client, target_channel_ids)

async def spam_channels_with_ping(client, channel_ids):
    guild = client.get_guild(1103328793218781234)

    if not guild:
        print('Guild not found.')
        return

    role = discord.utils.get(guild.roles, id=role_id)
    if not role:
        print('Role not found.')
        return

    for channel_id in channel_ids:
        channel = discord.utils.get(guild.channels, id=channel_id)
        if channel and isinstance(channel, discord.TextChannel) and channel.permissions_for(guild.me).send_messages:
            await channel.send(f'<@&{role_id}> Join our main server: discord.gg/stWgVnBgHq')
            await asyncio.sleep(delay_between_pings)

client.run(token)
