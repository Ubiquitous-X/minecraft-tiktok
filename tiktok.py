from TikTokLive import TikTokLiveClient
from TikTokLive.events import CommentEvent, ConnectEvent, JoinEvent, LiveEndEvent
from mctools import RCONClient
import sys

# Check if livstream user argument has been sent
if len(sys.argv) > 1:
    livestream = sys.argv[1]
else:
    # If no argument is sent, throw error and exit
    print("Error: No username sent. Start the script with 'python tiktokpy username' (without @)")
    sys.exit(1)  # Exit with error code 1

rcon = RCONClient('localhost') # The adress of the Minecraft server

success = rcon.login('password')
if success:
    print('Connected to RCON')
    rcon.command("say RCON connected")
else:
    print("Couldn't connect to RCON")
    exit()

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@"+livestream)

# Define how you want to handle specific events via decorator
@client.on(ConnectEvent)
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)

@client.on(JoinEvent)
async def on_join(event: JoinEvent):
    print(f"{event.user.nickname} joined the stream")
    # Spawn a zombie named as the viewer who just joined the stream
    rcon.command("title @a actionbar {\"text\":\""+event.user.nickname+" joined the stream\", \"color\":\"aqua\"}")
    rcon.command("execute at @p run summon zombie ^5 ^ ^ {CustomNameVisible:1,CustomName:'{\"text\":\""+event.user.nickname+"\"}'}")

@client.on(CommentEvent)
async def on_comment(event: CommentEvent):
    # Show a comment on the actionbar title with green text
    rcon.command("title @a actionbar {\"text\":\""+event.user.nickname+" says: "+event.comment+"\", \"color\":\"green\"}")
    print(f"{event.user.nickname} -> {event.comment}")

@client.on(LiveEndEvent)
async def on_connect(event: LiveEndEvent):
    print(f"Livestream ended :(")

# Define handling an event via "callback"
client.add_listener("comment", on_comment)

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()