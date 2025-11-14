
# Discord Nuker

A simple python script to nuke a discord, and creates 30 channels once nuked. 



## How To Use

Edit the script with your text editor of choice. Insert your bot token. 

Edit line 44 if you want to change the amount of channels it creates. 

For example: 

for i in range(30): would change to for i in range(10): if you wanted to create 10 channels instead. 


!ping - Tests the bot can recieve your commands. 

!resetchannels 'NUKED' - Command to nuke the discord. The bot will then make channels with whatever you write after the command. 

For example:

!resetchannels YOU-HAVE-BEEN-NUKED



## Support

Submit a bug request if anything doesn't work and I will fix it ASAP.


## FAQ

#### What Intents Does My Bot Need?

All of them, if you have access to the bot token then you probably have access to perms. As long as the bot as the Message Intent and perms to edit categories then it should work.

#### It Doesn't Work?

Bot probably doesn't have the proper perms.
