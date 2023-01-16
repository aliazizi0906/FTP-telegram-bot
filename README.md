# FTP-telegram-bot
A Telegram bot project by Python to upload files from Telegram to the server using FTP protocol.

This is a Telegram bot and its working process is as follows:

![FlowChart](https://user-images.githubusercontent.com/112679395/212622979-a5846d0a-5df1-4dc5-ba30-9f0854527aa5.png)

# 1-Download
First, Download source files on a server equipped with Python

# 2-Install Python Librarys
You need 3 library to run this robot.(Pyrogram, aioftp, asyncio)
To install libraries, we follow two methods: manual installation and automatic installation.
manual installation:
* pip install Pyrogram
* pip install aioftp
* pip install asyncio

automatic installation:
* pip install -r requirements.txt

# 3-Config file config.py
You must enter some information in the config.py file.
* In line 4 : you must replace your api_id with 0000000.
* In line 5 : you need to replace your api_hash with e28cc5d85c66rr785422fe3bf50e61f
* In line 8 : you should replace your bot token that you received from botfather with 8569471455:JJkiyA6MmuB570F4t5yVLmi92tWRqQi6rty.
* In line 11 : you must specify a name for your robot session, which is not important and you can leave it alone.
* In line 15 : you must enter the bot's admin ID, which is a numeric value. You can get your numerical ID by sending a message to the @myidbot bot in Telegram.
* In line 18 : you must enter the numerical ID of the robot manufacturer so that the robot bugs are sent to the manufacturer so that its problems can be solved in the next versions. You can change it.
* In line 23 : When a file is sent to the bot, first that file is downloaded from the Telegram repository and stored in the bot's server. Here you need to specify its temporary storage path. For example, I set the bot to save the downloaded file in the current path (the path where config.py file is located).
* In line 27: you must specify the address of the file storage directory on the host to which you have FTP access.
* In line 31: you must enter the IP address of your FTP host.
* In line 32: You must enter your FTP access username.
* In line 33: You must enter your FTP access password
* In line 34: You must enter the address of your domain.
