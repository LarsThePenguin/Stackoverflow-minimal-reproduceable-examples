import discord, asyncio
import threading

TOKEN = "Enter Discord token here"
CHANNEL_ID = 1234567890
client = discord.Client(intents=discord.Intents.default())

def uploadFile(data):
    startTime = time.time()
    chunks = wrap(data, maxFileSize)
    messageIDs = []
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    for chunk in chunks:
        file = open("upldchk.tmp.txt", "w")
        file.write(chunk)
        file.close()
        messageTask = asyncio.create_task(channel.send(file=discord.File("upldchk.tmp.txt")))
        message = asyncio.get_event_loop().run_until_complete(messageTask)
        messageIDs.append(message.id)
        os.remove("upldchk.tmp.txt")
    global currentWriteSpeed, printCurrentWriteSpeed
    currentWriteSpeed += len(data)/(time.time() - startTime)
    printCurrentWriteSpeed = True
    return messageIDs
  
def main():
    IDs = uploadFile("Lorem Ipsum i think")
    print(IDs)

@client.event
async def on_ready():
	global channel
	channel = client.get_channel(CHANNEL_ID)
	print(f"{client.user} has connected to Discord.")
	threading.Thread(target=main).start()

client.run(TOKEN)
