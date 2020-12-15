#A SIMPLE DISCORDBOT WITH PYTHON

#First go to https://discordapp.com/developers
#Klick on "New Applikation" fill in the name anything you want
#Now klick on your application and go to the bot settings, klick on "Add Bot" and klick on "Yes, do it!"
#Now you will find the token, copy it and paste it in the end of the code where I write "put in the token of the bot"
#The next step is to go to the general information setttings and there you must copy the client id
#After that go to https://discord.com/oauth2/authorize?&client_id=(put in the client id without brankets)&scope=bot
#Now you can invite the bot to your server. I hope you have fun with the bot.

import discord

class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("I'm logged in.")

    #Wenn Nachricht gepostet wird
    async def on_message(self, message,random=None):
        print("Message from " + str(message.author) + " contains " + str(message.content))
        if message.author  == client.user:
            return
        if message.content.startswith("hi"):       #<==== you can put anything else there
            await message.channel.send("HI")       #if the message contains for example "hi" the bot sends you the message "HI" but fill free to put something else there
                                                   #and you can copy/paste the last if-clausel to make more messsages that the can send to you


client = MyClient()
client.run("put in the token of the bot")


#After all run this script :) and have fun with it.
