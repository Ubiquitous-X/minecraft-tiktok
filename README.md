# Minecraft-TikTokLive
This is not something made by me, it is merely a merge of the [TikTokLive](https://github.com/isaackogan/TikTokLive) library by [@isaackogan](https://github.com/isaackogan) and the [mctools](https://github.com/Owen-Cochell/mctools) library by [@Owen-Cochell](https://github.com/Owen-Cochell) 

## What does it do?

The script utilizes the power of two libraries - TikTokLive and mctools - to bring the world of TikTok and Minecraft together. TikTokLive is a Python library that provides access to the TikTok API. On the other hand, mctools is a library that provides tools for interacting with Minecraft servers and clients.

By combining these two libraries, the script creates an exciting integration between TikTokLive and Minecraft. This opens up new opportunities for creative expression, as well as new ways to interact with one another. As mctools makes it work with RCON commands, the script works for every Minecraft server without the need for any mods.

## How does it work?
The script uses the TikTokLive library to listen for events on a specific TikTok livestream. When an event occurs, it sends an RCON command to the Minecraft server. 

By default this script handles the events user join and user comment. When a new viewer enters the TikTok livestream, a zombie is spawned near the player with the `execute at @p run summon zombie` RCON command. The zombie has a custom name that is the same as the viewer that joined. If a viewer makes a comment, it is shown on the Minecraft screen with the `title @a actionbar` RCON command. 

## How to get started?
### 1.
Either use an already established server you run, or download the [official Minecraft server file.](https://www.minecraft.net/en-us/download/server)

In the Minecraft `server.properties` file, make sure to set:

```
enable-rcon=true # To enable RCON
rcon.password=password # The password to connect to RCON with
```
### 2.
Install the libraries TikTokLive and mctools either separately or with `pip install -r requirements.txt`

In the `tiktok.py` file set:
```
rcon = RCONClient('localhost') # The adress of your Minecraft server
livestream = "username" # The username of the livestream, without '@'
success = rcon.login('password') # Same password as in server.properties
```

### 3.
Run the Minecraft server file with `java -jar server.jar`

Run the TikTok script with `python tiktok.py`

Everything should now work as intended. 

## Now what?
Only your imagination is your limit. You can make a bunch of creepers spawn when a specific gift is sent, or give a random player a diamond for each new follower. You can make the script listen for specific keywords in the livestream comments and handle that. You can even send comments to the livestream from within Minecraft.

For detailed documentation of the libraries and what you can do, please check out:

[TikTokLive library](https://github.com/isaackogan/TikTokLive) by [@isaackogan](https://github.com/isaackogan)

[mctools library](https://github.com/Owen-Cochell/mctools) by [@Owen-Cochell](https://github.com/Owen-Cochell)

[List of Minecraft commands](https://minecraft.fandom.com/wiki/Commands)