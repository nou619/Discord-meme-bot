import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class Nouclient(discord.Client): 
    async def on_ready(self):
        print(f'{self.user} is online!')
    async def on_message(self,message):
         if message.author == self.user:
            return

         if message.content.startswith('$hello'):
            await message.channel.send('hi!')

         if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
# Create bot permissions
BotPermissions=discord.Intents.default()
BotPermissions.message_content = True

# Create bot instance
client = Nouclient(intents=BotPermissions)

# Run the bot 
client.run('replace with your actual token')
