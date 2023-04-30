'''
import discord

client = discord.Client()

# Initialize command and image variables
command = ""
image_url = ""
reply_message = ""

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global command, image_url, reply_message

    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Set command, image_url, and reply_message variables
    if message.content.startswith('!remember'):
        split_msg = message.content.split()
        if len(split_msg) == 4:
            command = split_msg[1]
            image_url = split_msg[2]
            reply_message = split_msg[3]
            await message.channel.send('I will remember that!')

    # Check if message matches remembered command
    if message.content == command:
        await message.channel.send(image_url)
        await message.channel.send(reply_message)

# Replace 'TOKEN' with your bot's token
client.run('MTEwMjAzNTA2NTMzODM0NzYwMA.GbgjUS.5z5bYNhjgscrYVG3ND-qdPpcuu20vZ83o9VIR8')
'''